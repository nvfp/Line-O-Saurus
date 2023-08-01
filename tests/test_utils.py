import unittest

from src.utils import num_approx


class TestUtils(unittest.TestCase):

    def test_num_approx(self):
        self.assertEqual(num_approx(0), '0')
        self.assertEqual(num_approx(1), '1')
        self.assertEqual(num_approx(3), '3')
        
        self.assertEqual(num_approx(17), '17')
        self.assertEqual(num_approx(333), '333')
        self.assertEqual(num_approx(999), '999')
        
        self.assertEqual(num_approx(1000), '1K')
        self.assertEqual(num_approx(1001), '1K')
        self.assertEqual(num_approx(1049), '1K')
        self.assertEqual(num_approx(1050), '1.1K')
        self.assertEqual(num_approx(1099), '1.1K')
        self.assertEqual(num_approx(1399), '1.4K')
        
        self.assertEqual(num_approx(999_000_000), '999M')
        self.assertEqual(num_approx(1_200_000_000), '1.2B')
        
        self.assertEqual(num_approx(356_351_352_642_742), '356.4T')


if __name__ == '__main__':
    unittest.main()