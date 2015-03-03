
import re

def split(v, sep):
    return v.split(sep)

def trim(v):
    return v.strip()

def join(v, sep = ''):
    return sep.join(v)

def format(v, template = None):
    return template.format(*v) if template != None else v

def capture(v, pattern, flags = 0):    
    rx = re.compile(pattern, flags)
    match = rx.match(v)
    return match.groups() if match else None

def search(v, pattern, flags = 0):
    rx = re.compile(pattern, flags)
    match = rx.search(v)
    return match.group(0) if match else None

def subs(v, pattern, repl, flags = 0):
    rx = re.compile(pattern, flags)
    result = rx.sub(repl, v)
    return result
