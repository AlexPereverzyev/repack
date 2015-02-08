
import unittest
import tests.flows.flow_test_base as tests
import repack

class FilterTest(tests.FlowTestBase):
        
    def test_filter_falses(self):
        '''send string and None, return string - pass'''        
        results = []
        s = tests.sink(results)
        next(s)        
        with (repack
                .echo()
                .filter(s)) as filt:            
            filt.send('a')
            filt.send(0)
            filt.send('b')
            filt.send(None)
            filt.send('c')
            
        self.assertSequenceEqual(['a', 'b', 'c'], results)
        
    def test_filter_falses_more_filters(self):
        '''send strings and 0, more filters, return strings  - pass'''
        results = []
        s = tests.sink(results)
        next(s)        
        with (repack
                .echo()
                .string()
                .reverse()
                .filter(s)) as filt:            
            filt.send('a')
            filt.send(0)
            filt.send('b')
            filt.send('c')
            
        self.assertSequenceEqual(['a', 'b', 'c'], results)
        
    def test_filter_falses_more_filters_chained(self):
        '''send strings and 0, more filters, chained, return strings  - pass'''
            
        results = []
        right = tests.sink(results)
        next(right)        
    
        filt = (repack
                .echo()
                .string()
                .reverse()
                .filter(right))
            
        left = tests.src(filt)
        next(left)
                
        left.send('X')
        left.send(0)
        left.send('Y')
        
        self.assertSequenceEqual(['X', 'Y'], results)