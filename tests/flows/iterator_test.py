
import unittest
import tests.flows.flow_test_base as tests
import repack

class RegeneratorTest(tests.FlowTestBase):
    
    def test_iterate_list(self):
        '''source generator - pass'''
        with (repack         
                .integer()
                .iterator(
                    iter(['1','2','3']))) as iterator:            
            r = []
            for v in iterator:
                r.append(v)
                
        self.assertSequenceEqual([1,2,3], r)
        
    def test_iterate_none(self):
        '''source None - fail'''
        with self.assertRaises(TypeError):
            with (repack         
                    .integer()
                    .iterator(
                        None)) as iterator:            
                for v in iterator:
                    pass
    
    def test_iterate_list_more_filters(self):
        '''source, more filters - pass'''
        with (repack         
                .integer()
                .string()
                .reverse()
                .integer()
                .iterator(
                    iter(['1','2','3']))) as iterator:            
            r = []
            for v in iterator:
                r.append(v)
                
        self.assertSequenceEqual([1,2,3], r)
        
    def test_iterate_chained(self):
        '''source generator, chained - pass'''

        left = tests.gen(iter(['1','2','3']))        
        iterator = (repack         
                    .integer()
                    .iterator(
                        left))
        right = tests.gen(iterator)    
            
        r = []
        for v in right:
            r.append(v)
                
        self.assertSequenceEqual([1,2,3], r)
        
    def test_reset_source(self):
        '''reset source using send - pass'''
        with (repack         
                .integer()
                .iterator(
                    iter(['1','2','3']))) as iterator:            
            iterator.send(iter(['11', '22', '33']))
            r = []
            for v in iterator:
                r.append(v)
                
        self.assertSequenceEqual([11,22,33], r)
    
    def test_reset_source_forin(self):
        '''reset source using send in for...in - pass'''
        with (repack         
                .integer()
                .iterator(
                    iter(['1','2','3']))) as iterator:            
            r = []
            for v in iterator.send(iter(['11', '22', '33'])):
                r.append(v)
                
        self.assertSequenceEqual([11,22,33], r)
        
    def test_reset_source_initeration(self):
        '''reset source using send in iteration - pass'''
        with (repack         
                .integer()
                .iterator(
                    iter(['1','2','3']))) as iterator:
            iterator.send(iter(['11', '33', '22']))
            r = []
            for v in iterator:
                r.append(v)
                if v == 11:
                    iterator.send(iter([22,33]))
                
        self.assertSequenceEqual([11,22,33], r)
        
    def test_reset_source_none(self):
        '''reset source using send(None) - fails'''
        with self.assertRaises(TypeError):
            with (repack         
                    .integer()
                    .iterator()) as iterator:
                iterator.send(None)
                r = []
                for v in iterator:
                    r.append(v)