
import repack

with (repack
        .reverse()
        .printout()
        .filter()) as f:
        
    f.send('olleH')
    f.send(None)
    f.send('!dlroW')