import unittest

from src.get_options import get_options


class TestGetOptions(unittest.TestCase):

    def test_only_type(self):
        
        ## Pass
        get_options(ONLY_TYPE='[".txt"]')
        get_options(ONLY_TYPE='[".txt", ".json"]')
        get_options(ONLY_TYPE='[".txt",".json",".py"]')
        
        ## Fail
        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE='true')
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')
        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE='{"a": 1}')
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')
        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE='[]')
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')
        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE='[1, 2, 3]')
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')
        with self.assertRaises(AssertionError) as ctx: get_options(ONLY_TYPE='["a", "b"]')
        self.assertEqual(str(ctx.exception), 'Invalid only-type value.')
    
    def test_ignore_type(self):
        
        ## Pass
        get_options(IGNORE_TYPE='[".txt"]')
        get_options(IGNORE_TYPE='[".txt", ".json"]')
        get_options(IGNORE_TYPE='[".txt",".json",".py"]')
        
        ## Fail
        with self.assertRaises(AssertionError) as ctx: get_options(IGNORE_TYPE='true')
        self.assertEqual(str(ctx.exception), 'Invalid ignore-type value.')
        with self.assertRaises(AssertionError) as ctx: get_options(IGNORE_TYPE='{"a": 1}')
        self.assertEqual(str(ctx.exception), 'Invalid ignore-type value.')
        with self.assertRaises(AssertionError) as ctx: get_options(IGNORE_TYPE='[]')
        self.assertEqual(str(ctx.exception), 'Invalid ignore-type value.')
        with self.assertRaises(AssertionError) as ctx: get_options(IGNORE_TYPE='[1, 2, 3]')
        self.assertEqual(str(ctx.exception), 'Invalid ignore-type value.')
        with self.assertRaises(AssertionError) as ctx: get_options(IGNORE_TYPE='["a", "b"]')
        self.assertEqual(str(ctx.exception), 'Invalid ignore-type value.')
    
    def test_header(self):
        
        ## Pass
        get_options(HEADER=__file__)
        
        ## Fail
        with self.assertRaises(AssertionError) as ctx: get_options(HEADER='foo')
        self.assertEqual(str(ctx.exception), 'Invalid header value.')
    
    def test_footer(self):
        
        ## Pass
        get_options(FOOTER=__file__)
        
        ## Fail
        with self.assertRaises(AssertionError) as ctx: get_options(FOOTER='foo')
        self.assertEqual(str(ctx.exception), 'Invalid footer value.')
    
    def test_num_shown(self):
        
        ## Pass
        get_options(NUM_SHOWN='1')
        get_options(NUM_SHOWN='10')
        get_options(NUM_SHOWN='1000')
        
        ## Fail
        with self.assertRaises(AssertionError) as ctx: get_options(NUM_SHOWN='0')
        self.assertEqual(str(ctx.exception), 'Invalid num-shown value.')
        with self.assertRaises(AssertionError) as ctx: get_options(NUM_SHOWN='true')
        self.assertEqual(str(ctx.exception), 'Invalid num-shown value.')
    
    def test_show_approx(self):

        ## Pass
        get_options(SHOW_APPROX='true')
        get_options(SHOW_APPROX='false')
        
        ## Fail
        with self.assertRaises(AssertionError) as ctx: get_options(SHOW_APPROX='')
        self.assertEqual(str(ctx.exception), 'Invalid show-approx value.')
        with self.assertRaises(AssertionError) as ctx: get_options(SHOW_APPROX='123')
        self.assertEqual(str(ctx.exception), 'Invalid show-approx value.')
        with self.assertRaises(AssertionError) as ctx: get_options(SHOW_APPROX='[1, 2, 3]')
        self.assertEqual(str(ctx.exception), 'Invalid show-approx value.')
    
    def test_card_titles(self):

        ## Pass
        get_options(CARD_TITLES='{"line": "foo"}')
        get_options(CARD_TITLES='{"line": "foo", "stat": "bar"}')
        get_options(CARD_TITLES='{"size": "foo", "type": "bar"}')
        get_options(CARD_TITLES='{"line": "foo", "type": "bar", "stat": "# baz", "size": "**boo**"}')
        
        ## Fail
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='true')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='[1, 2]')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='{}')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='{"foo": "bar"}')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='{"line": "foo", "bar": "baz"}')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_TITLES='{"line": 1}')
        self.assertEqual(str(ctx.exception), 'Invalid card-titles value.')
    
    def test_card_order(self):

        ## Pass
        get_options(CARD_ORDER='["line"]')
        get_options(CARD_ORDER='["line", "stat"]')
        get_options(CARD_ORDER='["line", "type", "stat"]')
        get_options(CARD_ORDER='["type", "stat", "line"]')
        get_options(CARD_ORDER='["type", "stat", "line", "size"]')

        ## Fail
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='true')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='{"a": 1}')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='[]')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='["foo"]')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='["line", "foo"]')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')
        with self.assertRaises(AssertionError) as ctx: get_options(CARD_ORDER='["line", "type", "line"]')
        self.assertEqual(str(ctx.exception), 'Invalid card-order value.')

    def test_show_credit(self):

        ## Pass
        get_options(SHOW_CREDIT='true')
        get_options(SHOW_CREDIT='false')
        
        ## Fail
        with self.assertRaises(AssertionError) as ctx: get_options(SHOW_CREDIT='')
        self.assertEqual(str(ctx.exception), 'Invalid show-credit value.')
        with self.assertRaises(AssertionError) as ctx: get_options(SHOW_CREDIT='123')
        self.assertEqual(str(ctx.exception), 'Invalid show-credit value.')
        with self.assertRaises(AssertionError) as ctx: get_options(SHOW_CREDIT='[1, 2, 3]')
        self.assertEqual(str(ctx.exception), 'Invalid show-credit value.')


if __name__ == '__main__':
    unittest.main()