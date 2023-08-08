import unittest

from src.engine.get_star_card import LANG, get_bars, writer


PACK = {
    'foo-bar-baz': 1500,
    'foo': 500,
    'foo-bar': 50,
    'bar': 5,
}
TOTAL = 2055


class Test__writer(unittest.TestCase):

    def test_num_shown(self):
        
        result = writer(1, False, '', TOTAL, PACK)
        expected = (
            f'```{LANG}\n'
            f'foo-bar-baz  1,500 stargazers  73%  {get_bars(1500, TOTAL)}\n'
            '```'
        )
        self.assertEqual(result, expected)

        result = writer(3, False, '', TOTAL, PACK)
        expected = (
            f'```{LANG}\n'
            f'foo-bar-baz  1,500 stargazers  73%  {get_bars(1500, TOTAL)}\n'
            f'foo            500 stargazers  24%  {get_bars(500, TOTAL)}\n'
            f'foo-bar         50 stargazers   2%  {get_bars(50, TOTAL)}\n'
            '```'
        )
        self.assertEqual(result, expected)

        result = writer(5, False, '', TOTAL, PACK)
        expected = (
            f'```{LANG}\n'
            f'foo-bar-baz  1,500 stargazers  73%  {get_bars(1500, TOTAL)}\n'
            f'foo            500 stargazers  24%  {get_bars(500, TOTAL)}\n'
            f'foo-bar         50 stargazers   2%  {get_bars(50, TOTAL)}\n'
            f'bar              5 stargazers   0%  {get_bars(5, TOTAL)}\n'
            '```'
        )
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()