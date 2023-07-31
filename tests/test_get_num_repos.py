import unittest

from src.get_num_repos import get_num_repos


class TestGetNumRepos(unittest.TestCase):

    def test_normal(self):
        raw = '[{"url":"https://github.com/foo/bar"},{"url":"https://github.com/foo/baz"}]'
        n = get_num_repos(raw)
        self.assertEqual(n, 2)

    def test_empty(self):
        raw = '[]'
        n = get_num_repos(raw)
        self.assertEqual(n, 0)

    def test_formatted(self):
        raw = '[{"url":"https://github.com/foo/bar"}, {"url":"https://github.com/foo/baz"}]'
        n = get_num_repos(raw)
        self.assertEqual(n, 2)


if __name__ == '__main__':
    unittest.main()