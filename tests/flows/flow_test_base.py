
import unittest

class FlowTestBase(unittest.TestCase):
    pass

def gen(src):
    for v in src:
        yield v

def sink(results):
  while True:
      r = (yield)
      results.append(r)

def src(filt):
  while True:
      v= (yield)
      filt.send(v)

def loop():
    while True:
        yield (yield) 
    
