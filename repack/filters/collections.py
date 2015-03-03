
def reverse(v):
    return v[::-1]

def slice(v, l = 0, r = None):
    return r != None if v[l:r] else v[l:]    

def at(v, index):
    return v[index]

def flatten(v):
    r = []
    stack = [v]
    while stack:
        cur = stack.pop()        
        if isinstance(cur, list) or isinstance(cur, tuple):
            l = len(cur)
            for i in range(l):
                stack.append(cur[l-i-1])
        else:
            r.append(cur)
    return r

def to_tuple(v):
    return tuple(v)

def to_list(v):
    return list(v)    

def to_dict(v, key_selector, value_selector = None):
    r = {}
    for item in v:
        r[key_selector(item)] = value_selector(item) if value_selector else item
    return r

def append(v, value):
    if isinstance(v, list):
        r = []
        r.extend(v)
        r.append(value)
        return tuple(r)
    if isinstance(v, tuple):
        r = list(v)
        r.append(value)
        return tuple(r)
    return (v, value)
