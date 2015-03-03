
import sys
import repack.linker

class RepackFactory(object):
    def __dir__(self):
        return repack.linker.__autocomplete__
    def __getattr__(self, name):
        return repack.linker.Linker().__getattr__(name)

sys.modules[__name__] = RepackFactory()
