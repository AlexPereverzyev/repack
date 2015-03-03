
import time

def echo(v):
    return v

def none(v):
    return None

def printout(v):
    print(v)
    return v

def sleep(v, sec):
    time.sleep(sec)
    return v

def broadcast(v, subscribers):
    if subscribers:
        for s in subscribers:
            s.send(v)
    return v
