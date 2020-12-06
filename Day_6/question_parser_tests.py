# Auto-generated unit test template by AutoUnit.
import unittest
import question_parser

class Test_question_parser(unittest.TestCase):
    def test_count_response(self):
        self.assertTrue(question_parser.count_response('abc') == 3)
        self.assertTrue(question_parser.count_response('abcx') == 4)
        self.assertTrue(question_parser.count_response('abcy') == 4)
        self.assertTrue(question_parser.count_response(['a', 'b', 'c']) == 3)
        self.assertTrue(question_parser.count_response(['a', 'b', 'b']) == 2)
        self.assertTrue(question_parser.count_response(['a', 'b', 'c', 'd']) == 4)


    def test_or_resp(self):
        self.assertTrue(question_parser.or_resp(['abcx', 'abcy', 'abcz']) == 6)
        self.assertTrue(question_parser.or_resp('abc') == 3)
        self.assertTrue(question_parser.or_resp(['abc']) == 3)
        self.assertTrue(question_parser.or_resp(['ab', 'ac']) == 3)
        self.assertTrue(question_parser.or_resp(['a', 'a', 'a', 'a']) == 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)