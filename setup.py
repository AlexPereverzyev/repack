
from distutils.core import setup

setup(
    name='Repack',
    version=open('repack/VERSION').read().strip(),
    description='Repack is a collection of well known Python utilities nicely packed together.',
    long_description = open('README.rst').read(),
    url='https://github.com/alexpereverzyev/repack',
    author='Alex Pereverzyev',
    maintainer='Alex Pereverzyev',
    maintainer_email='pereverzev.alex@gmail.com',
    license='MIT',
    platforms = [
        'Mac OS',
        'Linux',
        'Windows',
    ],
    classifiers = [
        'Environment :: Console',
        'Environment :: Web Environment',        
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: MIT License',        
        'Intended Audience :: Developers',        
        'Topic :: Software Development :: Libraries :: Python Modules',      
    ],
    requires = [
        'json',
        'pickle',
        're',
        'base64',
        'html',
        'urllib',
        'cgi',
        'binascii',
        'zlib',
        'lzma',
        'time',
        'hashlib',
        'hmac',
    ],
    packages = [
        'repack',
        'repack.filters',
        'repack.flows'
    ])