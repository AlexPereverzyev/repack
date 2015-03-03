
def _ignore(func):
    '''Marks function to be ignored by filters linker. '''
    func.ignore = True       
    return func

@_ignore
def prep(func):
    '''Coroutine bootstraper'''
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        next(cr)
        return cr
    return start

class GenWrap(object):
    '''
    Wraps generator to allow attributes and customization on generators.
    '''    
    def __init__(self, gen):
        self._gen = gen
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._gen:
            return next(self._gen)
        else:
            raise GeneratorExit()
        
    def next(self):
        return self.__next__()
    
    def send(self, value):
        try:
            if self._gen:
                self._gen.send(value)
        except StopIteration:
            self.close()
        
    def close(self):
        if self._gen:
            self._gen.close()
        
    def throw(self, type, value = None, traceback = None):
        if self._gen:
            self._gen.throw(type, value, traceback)
        
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, tb):
        self.close()
            
class FilterFunc(object):    
    def __init__(self, func):
        self.func = func
        self.args = None
        self.kwargs = None
        
class ResetGenerator(Exception):
    pass

class IterateGenerator(Exception):
    pass
