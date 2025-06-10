import unittest
import calc

class test_calc(unittest.TestCase):
    def test_sub(self):
        res = calc.sub(10,5)
        self.assertEqual(res, 15)
    

if __name__ == "__main__":
    unittest.main()