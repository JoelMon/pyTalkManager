__author__ = 'Joel Montes de Oca'

import unittest
import pyTalkManager.pyTalkManager as tm

class testMain(unittest.TestCase):
    def test_buttonTest(self):
        self.assertEquals(tm.buttonTest(), 'The command worked.')

if __name__ == '__main__':
    unittest.main(exit=False)
