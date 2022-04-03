import unittest
from test import support
from arrcsv import arr_to_csv

class TestArrayConvertsToCSV(unittest.TestCase):
    def test_1d_array_converts_to_csv(self):
        arr = [1, 2, 3, 4, 5, 6]
        csv = arr_to_csv(arr)
        self.assertEqual(csv, '1,2,3,4,5,6')

    def test_2d_array_converts_to_csv(self):
        arr = [[1, 2, 3], [4, 5, 6]]
        csv = arr_to_csv(arr)
        self.assertEqual(csv, '1,2,3\n4,5,6')
    
    def test_3d_array_converts_to_csv(self):
        arr = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
        csv = arr_to_csv(arr)
        self.assertEqual(csv, '1,2,3\n4,5,6\n7,8,9\n10,11,12')

class TestThrowsErrorOnInvalidArray(unittest.TestCase):
    def test_throws_error_on_invalid_array(self):
        with self.assertRaises(ValueError):
            arr = [[[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]]
            arr_to_csv(arr)


if __name__ == '__main__':
    unittest.main()
