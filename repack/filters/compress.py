
import zlib

def deflate(v, level = 6):    
    bytestream = zlib.compress(v, level)    
    return bytestream

def inflate(v):        
    stream = zlib.decompress(v)
    return stream

# todo: zip