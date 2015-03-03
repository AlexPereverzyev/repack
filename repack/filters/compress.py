
import zlib
import lzma

def deflate(v, level = 6):    
    bytestream = zlib.compress(v, level)    
    return bytestream

def inflate(v):        
    stream = zlib.decompress(v)
    return stream

def lzma_compress(v):
    return lzma.compress(v)

def lzma_decompress(v):
    return lzma.decompress(v)
