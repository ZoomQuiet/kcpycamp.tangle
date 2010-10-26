import unittest

import test_tinymmv

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_tinymmv.suite())
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')