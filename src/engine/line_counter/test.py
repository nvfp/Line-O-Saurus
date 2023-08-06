import unittest

import os

from src.engine.line_counter import line_counter


TEST_DIR = os.path.join(os.path.dirname(__file__), 'test_data')


class Test__line_counter(unittest.TestCase):

    def test(self):        
        result = line_counter(TEST_DIR)
        expected = 5
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()