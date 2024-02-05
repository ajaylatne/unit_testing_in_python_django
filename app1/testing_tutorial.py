import unittest


class MyTestClass(unittest.TestCase):
    # test cases
    # test name should start with test_
    def test_string_a(self):
        self.assertEqual('a'*4, 'aaaa')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('FOO'.isupper())

    def test_custom_error(self):         
        print(10/0)
         

if __name__ == '__main__': 
    unittest.main()
