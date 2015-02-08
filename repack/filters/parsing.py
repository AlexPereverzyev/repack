

def split(v, sep):
    return v.split(sep)

def trim(v):
    return v.strip()

def join(v, sep = ''):
    return sep.join(v)

def format(v, template = None):
    if template == None:
        return v
    return template.format(*v)

# todo: regex set