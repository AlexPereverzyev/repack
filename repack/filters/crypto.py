
import hashlib
import hmac

def md5(v):    
    h = hashlib.md5()
    h.update(v)    
    return h.digest()

def sha(v, shaName = 256):
    alg = 'SHA'+str(shaName)
    h = hashlib.new(alg)
    h.update(v)
    return h.digest()

def mac(v, secret, name = 'SHA256'):
    s = secret
    if isinstance(s, str):
        s = bytes(s, 'utf-8')
    hm = hmac.new(s, v, name)
    return hm.digest()

def derive(v, salt, shaName = 256, rounds = 100000):    
    s = salt
    if isinstance(s, str):
        s = bytes(s, 'utf-8')
    alg = 'SHA'+str(shaName)
    dk = hashlib.pbkdf2_hmac(alg, v, s, rounds)
    return dk


