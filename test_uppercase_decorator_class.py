import unittest
from unittest.mock import Mock
from uppercase_decorator_class import greeting, UppercaseDecorator


class TestUppercaseDecorator(unittest.TestCase):
    def test_greeting_function(self):
        result = greeting()
        self.assertEqual(result, "HEY, I AM MUHAMMAD IMRAN.")

    def test_decorator(self):
        mock_func = Mock()
        mock_func.return_value = "This is the mock Function"

        decorated = UppercaseDecorator(mock_func)

        result = decorated()
        mock_func.assert_called_once()

        self.assertEqual(result, "THIS IS THE MOCK FUNCTION")


if __name__ == "__main__":
    unittest.main()
