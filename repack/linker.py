
import repack.filters
import repack.flows

from repack.common import FilterFunc

class Linker(object):
    '''
    Links filters and flows into pipelines.
    '''    
    def __init__(self):
        self._all_filters = dir(repack.filters)
        self._all_flows = dir(repack.flows)
        self._filters = []
        self._flow = None

    def __getattr__(self, name):        
        f = None        
        if name in self._all_filters:
            f = getattr(repack.filters, name)
            self._filters.append(FilterFunc(f))
            return self._filter_trap
        
        elif name in self._all_flows:
            f = getattr(repack.flows, name)
            self._flow = f
            return self._flow_trap
        
        if not f:
            raise AttributeError('\'{0}\' object has no attribute \'{1}\''
                .format(self.__class__.__name__, name))

    def _filter_trap(self, *args, **kwargs):
        f = self._filters[-1]
        f.args = args
        f.kwargs = kwargs
        return self
    
    def _flow_trap(self, *args, **kwargs):
        return self._flow(self._filters, *args, **kwargs)