from numb import add,product
import unittest 

class test_numb(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(7, 3), 10)
        self.assertEqual(add(7), 9)
        self.assertEqual(add(5), 7)
    
    def test_product(self):
        self.assertEqual(product(5, 5), 25)
        self.assertEqual(product(5), 10)
        self.assertEqual(product(9), 18)

if __name__ == '__main__':
    unittest.main() 