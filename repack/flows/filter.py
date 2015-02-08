
'''
Pushes data through filter pipeline to the specified sink,
unless filter function returns value interpreted as False.
    
Can be easily chained with any other pipeline.
'''

from repack.common import *

def filter(filters, sink = None):
    source = sink

    for f in reversed(filters):
        source = FilterFlow.link(f, source)
        
    flow = FilterFlow(source)
    return flow

class FilterFlow(GenWrap):
    
    @staticmethod
    @prep
    def link(filt, sink = None):
        try:        
            while True:
                v = (yield)
                if v:
                    v = filt.func(v, *filt.args, **filt.kwargs)
                if sink and v:
                   sink.send(v)                
                
        except GeneratorExit:
            if sink:
               sink.close() 