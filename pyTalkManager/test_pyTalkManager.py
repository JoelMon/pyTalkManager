__author__ = 'JoelMontes de Oca'

import unittest
import pyTalkManager as tm

class MyTestCase(unittest.TestCase):

    def test_button_test(self):
        self.assertEquals(tm.buttonTest(), 'The command worked.')

if __name__ == '__main__':
    unittest.main(exit=False)
