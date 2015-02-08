
==================
Welcome to Repack!
==================

Repack is a collection of well known utilities nicely packed together.
To illustrate the idea, imagine, you need to pass an object via URL query
string, with Repack it looks like::
    
    import repack

    token1 = (repack
                .json_encode()
                .bytify()
                .deflate()
                .base64_encode()
                .url_encode()        
                .converter()
                .send({'id': 10001, 'desc':'this is a token' }))

But normally, you would do::

    import json
    import zlib
    import base64
    import urllib.parse
    
    string = json.dumps({'id': 10001, 'desc':'this is a token' })
    stream = bytes(string, 'utf-8')
    stream = zlib.compress(stream)
    string = base64.b64encode(stream)
    token1 = urllib.parse.quote(string)

Feel the difference :) Also you want it to be lasy, so you can make a converter
once and use it later::

    urlit = (repack
                .json_encode()
                .bytify()
                .deflate()
                .base64_encode()
                .url_encode()        
                .converter())
                
Like this::

    token1 = urlit.send({'id': 10001, 'desc':'this is a token' })
    
Or like this::

    token2 = urlit.send('another token lol')    
    token3 = urlit.send('one more yay')
    token4 = urlit.send('yay!!!')

You can chain the utilities as filter, meaning, values interpreted as `False`
will not pass::

    with (repack
            .reverse()
            .printout()
            .filter()) as f:
            
        f.send('olleH')
        f.send(None)
        f.send('!dlroW')
        f.send(None)
        
Prints::

    Hello
    World!
    
Another example is iterator, which allows to set source later::

    with (repack
            .trim()
            .integer()
            .iterator()) as iterator:
            
        results = []
        for v in iterator.send(iter(['1 ','\t2', '\n3'])):
            results.append(v)
        
Results in::

    [1, 2, 3]

Or vice versa, using accumulator::

    with (repack
            .trim()
            .integer()
            .accumulator()) as acc:
        
        acc.send('1 ')
        acc.send('\t2')
        acc.send('\n3')
        
        results = []
        for v in acc:
            results.append(v)

The package is under development. Everyone is welcome to contribute.
For TODOs, please see the current TODO list in the root folder.

Requirements
============

- Python 3.4.2

Install
=======

(This has not been published yet)

sudo pip install repack 

Extension
=========

As easy as adding more filters to `filters/__init__.py` or more flows
to `flows/__init__.py`.