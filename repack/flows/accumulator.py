
'''
Sends data to generator pipeline and accumulates results. 
The results can be iterated later in a separate for..in loop.

Items can be `send` to accumulator during iteration, which results
in appending the items to accumulator's source. Can be chained with
any coroutine pipeline or, as a source, with other generator pipeline.
'''

from repack.common import *

def accumulator(filters, sink = None):        
    acc = AccumulatorFlow.acc(sink)
    source = acc

    for f in reversed(filters):            
        source = AccumulatorFlow.link(f, source)
        
    flow = AccumulatorFlow(source, acc)
    return flow

class AccumulatorFlow(GenWrap):

    def __init__(self, src, acc):
        super(AccumulatorFlow, self).__init__(src)
        self._acc = acc

    def __iter__(self):
        try:
            self._acc.throw(IterateGenerator)
        except IterateGenerator:
            pass
        return self

    def __next__(self):        
        return next(self._acc)
    
    def send(self, value):
        try:
            self._acc.throw(ResetGenerator)
            self._gen.send(value)  
        except ResetGenerator:
            pass
       
    @staticmethod 
    @prep
    def link(filt, sink):
        try:        
            while True:
                v = (yield)
                v = filt.func(v, *filt.args, **filt.kwargs)
                v = sink.send(v)
        except GeneratorExit:
            sink.close()
            
    @staticmethod
    @prep
    def acc(sink = None):        
        items = []
        iterator = iter(items)
        acc = 1        
        while True:
            try:
                if acc:
                    v = (yield)
                    items.append(v)
                    if sink:
                       sink.send(v)                
                yield
                
                for v in iterator:
                    yield v                    
                break
            
            except IterateGenerator:                
                acc = 0
                continue
            
            except ResetGenerator:                
                acc = 1
                continue
            
            except GeneratorExit:
                if sink:
                   sink.close()
                break 