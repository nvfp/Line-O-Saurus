import unittest

from src.engine.pb_maker import progress_bars_maker


class Test__progress_bars_maker(unittest.TestCase):

    def test(self):

        result = progress_bars_maker(1, 10, 'X', 10)
        expected = 'X'*1 + ' '*9
        self.assertEqual(result, expected)

        result = progress_bars_maker(0, 10, 'X', 10)
        expected = 'X'*0 + ' '*10
        self.assertEqual(result, expected)

        result = progress_bars_maker(10, 10, 'X', 10)
        expected = 'X'*10 + ' '*0
        self.assertEqual(result, expected)

        result = progress_bars_maker(5, 10, 'X', 100)
        expected = 'X'*50 + ' '*50
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()