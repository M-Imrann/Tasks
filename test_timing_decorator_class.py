import unittest
from timing_decorator_class import slow, medium, fast


class TestTimingDecorator(unittest.TestCase):
    '''
    Test Timing Decorator to test the timing decorator.
    '''
    def test_slow_function(self):
        '''
        Testing slow function.
        '''
        result = slow()
        self.assertEqual(result, "Slow Function Executed.")

    def test_medium_function(self):
        '''
        Testing Medium function.
        '''
        result = medium()
        self.assertEqual(result, "Medium Function Executed.")

    def test_fast_function(self):
        '''
        Testing Fast function.
        '''
        result = fast(5)
        self.assertEqual(result, "Fast Function Executed.")


if __name__ == "__main__":
    unittest.main()
