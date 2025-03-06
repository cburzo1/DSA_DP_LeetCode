import unittest
import main

class TestMain(unittest.TestCase):
    def test_sumRange(self):
        NumArray = main.NumArray([-2, 0, 3, -5, 2, -1])
        result = NumArray.sumRange(0,2)
        self.assertEqual(result, 1)
        result = NumArray.sumRange(2, 5)
        self.assertEqual(result, -1)
        result = NumArray.sumRange(0, 5)
        self.assertEqual(result, -3)
        #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
