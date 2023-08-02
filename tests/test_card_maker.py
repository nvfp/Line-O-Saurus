import unittest

from src.card_maker import card_maker


class TestCardMaker(unittest.TestCase):

    def test_no_title(self):

        entries = [
            ['foo', '43%', '323,123 lines', 'XXXXXXXXXXXXXXX'],
            ['foooooooo', '3%', '323 lines', 'XXXXXXX'],
            ['a', '100%', '3 lines', 'XXXX'],
        ]
        align = [-1, 1, 1, -1]
        result = card_maker(None, entries, align)
        expected = (
            'foo         43%  323,123 lines  XXXXXXXXXXXXXXX\n'
            'foooooooo    3%      323 lines  XXXXXXX\n'
            'a          100%        3 lines  XXXX'
        )
        self.assertEqual(result, expected)

    def test_with_title(self):

        entries = [
            ['foo', '43%', '323,123 lines', 'XXXXXXXXXXXXXXX'],
            ['foooooooo', '3%', '323 lines', 'XXXXXXX'],
            ['a', '100%', '3 lines', 'XXXX'],
        ]
        align = [-1, 1, 1, -1]
        result = card_maker('# Foo bar', entries, align)
        expected = (
            '# Foo bar\n\n'
            'foo         43%  323,123 lines  XXXXXXXXXXXXXXX\n'
            'foooooooo    3%      323 lines  XXXXXXX\n'
            'a          100%        3 lines  XXXX'
        )
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()