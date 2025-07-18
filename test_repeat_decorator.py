import unittest
from unittest.mock import patch
from repeat_decorator import repeat


class TestRepeatDecorator(unittest.TestCase):
    def test_repeat(self):
        '''
        Test case for repeat function
        '''
        @repeat(3, print_result=True)
        def greeting(name):
            return f"Hi {name}"

        with patch("builtins.print") as mock_print:
            result = greeting("Ali")

        # Assert that print was called 3 times
        self.assertEqual(mock_print.call_count, 3)
        mock_print.assert_any_call("Hi Ali")
        self.assertEqual(result, ["Hi Ali", "Hi Ali", "Hi Ali"])


if __name__ == "__main__":
    unittest.main()
