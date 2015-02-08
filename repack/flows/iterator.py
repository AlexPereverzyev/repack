
'''
Pulls data from the specified source via generator pipeline.
Source can be specified later one or more times. Also source can be
reset during iteration.
    
Can be chained with other generator pipelines, however chain can be
broken if `send` method is used to set source.
'''

from repack.common import *

def iterator(filters, src = None):
    iter_src = IteratorFlow.src(src)
    source = iter_src
    
    for f in filters:
        source = IteratorFlow.link(f, source)
        
    flow = IteratorFlow(source, iter_src)
    return flow
    
class IteratorFlow(GenWrap):
    
    def __init__(self, gen, src):
        super(IteratorFlow, self).__init__(gen)
        self._src = src
    
    def __iter__(self):
        try:
            self._src.throw(IterateGenerator)
        except IterateGenerator:
            pass
        return self
    
    def send(self, value):
        try:
            self._src.throw(ResetGenerator)        
            self._src.send(value)
        except ResetGenerator:
            pass
        return self._gen

    @staticmethod
    @prep
    def src(source = None):
        empty = 1
        while True:
            try:
                if empty:
                    s = (yield)
                    source = s
                yield
                
                for v in source:
                    yield v
                empty = 0
                break
            
            except IterateGenerator:
                empty = 0
                continue
            
            except ResetGenerator:
                empty = 1
                continue
            
            except GeneratorExit:
                if source:
                   source.close()
                break

    @staticmethod
    def link(filt, source = None):
        try:
            for v in source:
                v = filt.func(v, *filt.args, **filt.kwargs)
                yield v                
        except GeneratorExit:
            if source:
               source.close()