import unittest
from payment_processor import PaymentProcessor


class TestPaymentProcessor(unittest.TestCase):
    '''
    The class is for testing the Payment processor.
    '''
    def setUp(self):
        self.processor = PaymentProcessor()

    def test_valid_amount(self):
        '''
        test_valid_amount function test that the amount is valid or not.
        '''
        result = self.processor.process_payment(1000)
        self.assertEqual(result, 1020.00)

    def test_zero_amount(self):
        '''
        test_zero_amount function test that the amount is zero.
        '''
        with self.assertRaises(ValueError):
            self.processor.process_payment(0)

    def test_negative_amount(self):
        '''
        test_negative_amount function test that the amount is negative.
        '''
        with self.assertRaises(ValueError):
            self.processor.process_payment(-58)

    def test_exceed_limit(self):
        '''
        test_exceed_amount function test if the amount exceeds the limit.
        '''
        with self.assertRaises(ValueError):
            self.processor.process_payment(10000)

    def test_fee_rounding(self):
        '''
        test_fee_rounding function test that the outcome
        is correct as expected.
        '''
        result = self.processor.process_payment(145.34)
        expected = round(145.34 * 1.02, 2)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
