
def integer(v):
    return int(v)

def string(v, encoding = 'utf-8'):
    if isinstance(v, bytes):
        return v.decode(encoding)
    return str(v)

def bytify(v, encoding = 'utf-8'):
    return bytes(v, encoding)