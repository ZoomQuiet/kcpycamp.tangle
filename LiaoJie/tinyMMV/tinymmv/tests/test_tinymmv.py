#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tinymmv.tinymmv import TinyMmv

import unittest

class TinyMmvTestCase(unittest.TestCase):

    def setUp(self):
        self.tinymmv = TinyMmv()

    def tearDown(self):
        pass

    def test_getRows(self):
        rows = self.tinymmv.getRows()
        self.assertEqual([[1,"a"], [2,"b"], [3,"c"]], rows)

    def test_setRows(self):
        rowsNew = [[11,"aa"], [12,"bb"], [13,"cc"]]
        self.tinymmv.setRows(rowsNew)
        rows = self.tinymmv.getRows()
        self.assertEqual(rowsNew, rows)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TinyMmvTestCase, 'test'))
    return suite

if __name__ == '__main__':
    unittest.main()