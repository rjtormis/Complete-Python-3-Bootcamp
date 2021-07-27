import unittest
import cap
# Using Unit Test
class testcap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result=cap.cap_text(text)
        self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
    unittest.main()