#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Name:         tinymmv.py
# Purpose:      just for test bitten
#
# Author:       Richard Liao <richard.liao.i@gmail.com>
#
#----------------------------------------------------------------------------

"""Tiny MMV module."""

class TinyMmv(object):
    """Represents a table."""
    def __init__(self):
        """Initialize tiny mmv.
        """
        self.rows = [[1,"a"], [2,"b"], [3,"c"]]

    def getRows(self):
        """Retrieve rows.
        """
        return self.rows

    def setRows(self, rows):
        """Set rows.
        """
        self.rows = rows

if __name__ == "__main__":
    tinyMmv = TinyMmv()
    rows = tinyMmv.getRows()
    print "Default rows:"
    print rows

    rowsNew = [[11,"aa"], [12,"bb"], [13,"cc"]]
    tinyMmv.setRows(rowsNew)
    rows = tinyMmv.getRows()
    print "New rows:"
    print rows
