import unittest
import my_functions

class TestMyFunc(unittest.TestCase):
 
    def setUp(self):
        pass 

    def test_multliply_by_two(self): 
        self.assertEqual(  my_functions.multliply_by_two(4), 8)

    def test_multliply_by_ten(self):
        self.assertEqual( my_functions.multliply_by_ten(10), 100)

if __name__ == '__main__':
    unittest.main()
