#!/usr/bin/env python
# -*- coding: utf-8 -*-
#单独运行需要将tinymmv模块放在这个文件的文件夹中


from tinymmv import TinyMmv

import unittest

class TinyMmvTestCase(unittest.TestCase):
    # 可以通过覆盖runTest方法即可得到最简单的测试用例子类以运行一些测试代码
    # setUp,一般用来设置 ，测试框架会在运行测试时自动调用此方法
    # 如果setUp 方法在测试中运行抛异常，框架会认为测试遇到了错误，并runTest不会被执行
   
    def setUp(self):
        """Test tinyMmv"""
        self.tinymmv = TinyMmv()
    # tearDown 方法用来完成runTest运行后的清理工作
    # 如果setUp 执行成功，无论runTest是否成功，tearDown都将执行
    def tearDown(self):
        pass

    def test_getRows(self): #  测试getRows()
        rows = self.tinymmv.getRows()
        
        self.assertEqual([[1,"a"], [2,"b"], [3,"c"]], rows)

    def test_setRows(self):#  测试setRows()
        rowsNew = [[11,"aa"], [12,"bb"], [13,"cc"]]

        self.tinymmv.setRows(rowsNew)

        rows = self.tinymmv.getRows()

        self.assertEqual(rowsNew, rows)

#suite 套件、
def suite():

    suite = unittest.TestSuite()
    #makeSuite 创建一个由测试用例来测试用例组成的套件
    #实际上是是将TinyMmvTestCase 中的函数运行一边
    #每个测试用例的顺序是测试方法名根据Python内建函数CMP所排序的顺序来决定的
    #cmp(x,y)  Return negative if x<y, zero if x==y, positive if x>y.
    #addTest 是将测试套件加入测试
    suite.addTest(unittest.makeSuite(TinyMmvTestCase, 'test'))

    return suite
#除了上面的函数suite()外，还可采用下代码
#class TinyTestSuite(unittest.TestSuite):
#    def __init__(self):
#        unittest.TestSuite.__init__(self,map(TinyMmvTestCase,("test_getRows","test_setRows")))

if __name__ == '__main__':
    unittest.main()
