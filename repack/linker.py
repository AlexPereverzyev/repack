
import repack.filters
import repack.flows

from repack.common import FilterFunc

__all_filters__ = None 
__all_flows__ = None
__autocomplete__ = None
__ignore_flag__ = 'ignore'
__initialized__ = 0

if not __initialized__:
    '''Filter out everything but functions from filters/flows.'''
    def filter_modules(modules):
        import re
        import types
        import_pattern = re.compile('^[^_]{1,2}.+')
        return [m for m in dir(modules)
                  if import_pattern.match(m) and
                     isinstance(getattr(modules, m), types.FunctionType) and
                     not hasattr(getattr(modules, m), __ignore_flag__)]
    
    __all_filters__ = filter_modules(repack.filters)
    __all_flows__ = filter_modules(repack.flows)
    __autocomplete__ = __all_filters__ + __all_flows__
    __initialized__ = 1

class Linker(object):
    '''
    Links filters and flows into pipelines.
    '''    
    def __init__(self):
        self._filters = []
        self._flow = None

    def __dir__(self):
        return __autocomplete__

    def __getattr__(self, name):
        f = None        
        if name in __all_filters__:
            f = getattr(repack.filters, name)
            self._filters.append(FilterFunc(f))
            return self._filter_trap
        
        elif name in __all_flows__:
            f = getattr(repack.flows, name)
            self._flow = f
            return self._flow_trap
        
        if not f:
            raise AttributeError('Repack has no filter or flow \'{0}\''
                .format(name))

    def _filter_trap(self, *args, **kwargs):
        f = self._filters[-1]
        f.args = args
        f.kwargs = kwargs
        return self
    
    def _flow_trap(self, *args, **kwargs):
        return self._flow(self._filters, *args, **kwargs)
