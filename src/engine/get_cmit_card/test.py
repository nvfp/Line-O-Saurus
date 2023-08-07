import unittest

from src.engine.get_star_card import LANG, writer


PACK = {
    'foo-bar-baz': 1500,
    'foo': 500,
    'foo-bar': 50,
    'bar': 5,
}
TOTAL = 2055


class Test__writer(unittest.TestCase):

    def test_num_shown(self):
        
        result = writer(1, False, None, TOTAL, PACK)
        expected = (
            f'```{LANG}\n'
            'foo-bar-baz  1500 stargazers  73%  ⭐️🌟⭐️🌟⭐️🌟⭐️🌟⭐️\n'
            '```'
        )
        self.assertEqual(result, expected)
        
        result = writer(3, False, None, TOTAL, PACK)
        expected = (
            f'```{LANG}\n'
            'foo-bar-baz  1500 stargazers  73%  ⭐️🌟⭐️🌟⭐️🌟⭐️🌟⭐️\n'
            'foo           500 stargazers  25%  ⭐️🌟⭐️         \n'
            'foo-bar        50 stargazers   2%                \n'
            '```'
        )
        self.assertEqual(result, expected)
        
        result = writer(5, False, None, TOTAL, PACK)
        expected = (
            f'```{LANG}\n'
            'foo-bar-baz  1500 stargazers  73%  ⭐️🌟⭐️🌟⭐️🌟⭐️🌟⭐️\n'
            'foo           500 stargazers  25%  ⭐️🌟⭐️         \n'
            'foo-bar        50 stargazers   2%                \n'
            'bar             5 stargazers   0%                \n'
            '```'
        )
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()