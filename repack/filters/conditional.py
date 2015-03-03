
def map(v, mapping):    
    return mapping[v] if mapping != None and v in mapping else None

def ifelse(v, func, if_case = None, else_case = None):
    r = func(v) if func else v
    return if_case if r else else_case
