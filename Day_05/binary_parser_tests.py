# Auto-generated unit test template by AutoUnit.
import unittest
import binary_parser

class Test_binary_parser(unittest.TestCase):
    def test_parse_seat(self):
        self.assertTrue(binary_parser.parse_seat('FBFBBFFRLR') == (44, 5))
        self.assertTrue(binary_parser.parse_seat('BFFFBBFRRR') == (70, 7))
        self.assertTrue(binary_parser.parse_seat('FFFBBBFRRR') == (14, 7))
        self.assertTrue(binary_parser.parse_seat('BBFFBBFRLL') == (102, 4))

    def test_bin_parse(self):
        pass

    def test_get_seat_id(self):
        self.assertTrue(binary_parser.get_seat_id(binary_parser.parse_seat('FBFBBFFRLR')) == 357)
        self.assertTrue(binary_parser.get_seat_id(binary_parser.parse_seat('BFFFBBFRRR')) == 567)
        self.assertTrue(binary_parser.get_seat_id(binary_parser.parse_seat('FFFBBBFRRR')) == 119)
        self.assertTrue(binary_parser.get_seat_id(binary_parser.parse_seat('BBFFBBFRLL')) == 820)


if __name__ == '__main__':
    unittest.main(verbosity=2)