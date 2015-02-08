
'''
Sends data to coroutine pipeline and immediatly returns result.

Data is sent all the way to the last coroutine and back,
thus can be chained with coroutines which yield value back.
'''

from repack.common import *

def converter(filters, sink = None):
    source = sink

    for f in reversed(filters):
        source = ConverterFlow.link(f, source)
        
    flow = ConverterFlow(source)
    return flow

class ConverterFlow(GenWrap):

    def send(self, value):
        if self._gen:
            next(self._gen)
            v = self._gen.send(value)        
            return v
        return None

    @staticmethod
    def link(filt, sink = None):
        try:        
            while True:
                v = (yield)
                v = filt.func(v, *filt.args, **filt.kwargs)
                if sink:
                    next(sink)
                    v = sink.send(v)                
                yield v            
        except GeneratorExit:
            if sink:
               sink.close() 