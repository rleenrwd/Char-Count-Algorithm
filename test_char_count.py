import unittest
from main import charCount

class TestCharCount(unittest.TestCase):
    
    def test_basic_input(self):
        result = charCount("Hello")
        expected = {'h':1, 'e':1, 'l':2, 'o':1}
        self.assertEqual(result, expected)

    def test_ignore_spaces_punc(self):
        result = charCount("Hello, World!")
        expected = {'h':1, 'e':1, 'l':3, 'o':2, 'w':1, 'r':1, 'd': 1}
        self.assertEqual(result, expected)

    def test_numbers_and_letters(self):
        result = charCount("abc123")
        expected = {'a':1, 'b':1, 'c':1, '1':1, '2':1, '3':1}
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()