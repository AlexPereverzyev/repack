
import sys
import repack.linker

class RepackFactory(object):    
    def __getattr__(self, name):
        return repack.linker.Linker().__getattr__(name)
    
sys.modules[__name__] = RepackFactory()