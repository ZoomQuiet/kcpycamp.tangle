import unittest

import test_kchhd_orm

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_kchhd_orm.suite())
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suite')
