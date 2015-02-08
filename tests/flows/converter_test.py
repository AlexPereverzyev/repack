
import unittest
import tests.flows.flow_test_base as tests
import repack

class ConverterTest(tests.FlowTestBase):
    
    def test_convert_int(self):
        '''convert int to str - pass'''
        with (repack
                .integer()        
                .converter()) as c:
            r = c.send('101010')
            
        self.assertEqual(101010, r)
        
    def test_convert_int_more_filters(self):
        '''convert int to str, more filters - pass'''
        with (repack
                .reverse()
                .integer()
                .converter()) as c:
            r = c.send('1212')
            
        self.assertEqual(2121, r)
        
    def test_convert_int_more_values(self):
        '''convert few values - pass'''
        results = []
        with (repack
                .reverse()
                .integer()
                .converter()) as c:
            results.append(c.send('1234'))
            results.append(c.send('123'))
            results.append(c.send('12'))
            
        self.assertSequenceEqual([4321, 321, 21], results)
        
    def test_convert_int_more_chained(self):
        '''convert int to str, more filters, chained - pass'''
        results = []
        right = tests.loop()
        with (repack
                .reverse()
                .integer()
                .converter(right)) as c:
            results.append(c.send('3'))
            results.append(c.send('2'))
            results.append(c.send('1'))
            
        self.assertSequenceEqual([3, 2, 1], results)