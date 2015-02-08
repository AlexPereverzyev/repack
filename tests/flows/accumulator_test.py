
import unittest
import tests.flows.flow_test_base as tests
import repack

class AccumulatorTest(tests.FlowTestBase):
    
    def test_acc_sum(self):
        '''send ints, calc sum - pass'''
        with (repack
                .integer()
                .accumulator()) as acc: 
            acc.send('1')
            acc.send('2')
            acc.send('3')
            
            result = sum(acc)
        
        self.assertEquals(6, result)
        
    def test_acc_iterate(self):
        '''send int, string, iterate - pass'''
        with (repack
                .echo()
                .accumulator()) as acc: 
            acc.send(1213123)
            acc.send('text')
            acc.send(None)
            
            results = []
            for v in acc:
                results.append(v)
                
        self.assertSequenceEqual([1213123, 'text', None], results)

    def test_acc_iterate_senditem(self):
        '''send ints, iterate, send item during iteration twice - pass'''
        with (repack
                .echo()
                .accumulator()) as acc:             
            
            acc.send('ping')
            acc.send('ping')
            
            results = []
            for v in acc:
                results.append(v)
                if v == 'ping':
                    acc.send('pong')

        self.assertSequenceEqual(['ping', 'ping', 'pong', 'pong'], results)
        
        
    def test_acc_iterate_senditem_chained(self):
        '''send ints, iterate, send item during iteration, chained - pass'''
        with (repack
                .echo()
                .reverse()
                .reverse()
                .accumulator()) as acc:             
            
            acc.send('yo')
            acc.send('yo')
            
            g1 = tests.gen(acc)
            cr1 = tests.src(acc)
            next(cr1)
            results = []
            for v in g1:
                results.append(v)
                if v == 'yo':
                    cr1.send('yo!')

        self.assertSequenceEqual(['yo', 'yo', 'yo!', 'yo!'], results)