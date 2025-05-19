import unittest
from main import charCount

class TestCharCount(unittest.TestCase):
    
    def test_basic_input(self):
        result = charCount("Hello")
        expected = {'h':1, 'e':1, 'l':2, 'o':1}
        self.assertEqual(result, expected)




if __name__ == "__main__":
    unittest.main()