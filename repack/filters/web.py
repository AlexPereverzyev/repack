
import html.parser
import urllib.parse
import cgi
import base64
import binascii

def url_encode(v):
    return urllib.parse.quote(v)

def url_decode(v):
    return urllib.parse.unquote(v)

def html_encode(v):
    return cgi.escape(v)

def html_decode(v):
    parser = html.parser.HTMLParser()
    return parser.unescape(v)

def base64_encode(v, altchars = None):
    a = altchars
    if isinstance(a, str):
        a = bytes(a, 'utf-8')
    return base64.b64encode(v, a)

def base64_decode(v, altchars = None):
    a = altchars
    if isinstance(a, str):
        a = bytes(a, 'utf-8')
    return base64.b64decode(v, a)

def hexlify(v):
    return binascii.hexlify(v)

def unhexlify(v):
    return binascii.unhexlify(v)
