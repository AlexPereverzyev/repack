
def reverse(v):
    return v[::-1]

def slice(v, l = 0, r = None):
    if r == None:
        return v[l:]
    return v[l:r]

def flatten(v):
    r = []
    stack = [v]
    while stack:
        cur = stack.pop()
        l = len(cur)
        if isinstance(cur, list):
            for i in range(l):
                stack.append(cur[l-i-1])
        else:
            r.append(cur)
    return r

# todo
# to dict
# to list
# to tuple