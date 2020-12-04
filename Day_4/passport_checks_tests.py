import unittest
import passport_checks

class test_passport_methods(unittest.TestCase):
    def test_birth(self):
        self.assertTrue(passport_checks.check_birth('2002'))
        self.assertFalse(passport_checks.check_birth('2003'))

    def test_height(self):
        self.assertTrue(passport_checks.check_height('60in'))
        self.assertTrue(passport_checks.check_height('190cm'))
        self.assertFalse(passport_checks.check_height('190in'))
        self.assertFalse(passport_checks.check_height('190'))

    def test_hair(self):
        self.assertTrue(passport_checks.check_hair('#123abc'))
        self.assertFalse(passport_checks.check_hair('#123abz'))
        self.assertFalse(passport_checks.check_hair('123abc'))

    def test_eye(self):
        self.assertTrue(passport_checks.check_eye('brn'))
        self.assertFalse(passport_checks.check_eye('wat'))

    def test_id(self):
        self.assertTrue(passport_checks.check_id('000000001'))
        self.assertFalse(passport_checks.check_id('0123456789'))

if __name__ == '__main__':
    unittest.main()