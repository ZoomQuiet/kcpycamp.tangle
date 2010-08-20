# coding: UTF-8
#!/usr/bin/python
# Filename: BehindColon.py

"""
@author: 方正圆
@license: kcCCRJ
@version：1.0
@tag：判断case,default的:后是否有注释，空格以外的东西

@param CodeLine：需检测的字符串 
@type CodeLine: 字符串
@param Start: 从该行字符串的第几个位置开始检测
@type Start: 整型
@return: 若有注释，空格以外的东西则返回False，否则返回True
@rtype : bool
"""
def behindcolon(CodeLine,start):
    k = len(CodeLine)
    i = start
    markColon = False
    markRemark = False
    while i < k - 2:
        i = i + 1
        if i < k - 1:
            sTemp = CodeLine[i:i+2]
            if '//' == sTemp:
                return (True == markColon)
            elif '/*' == sTemp:
                markRemark = True
        if False == markRemark:
            if False == markColon:
                if ':' == CodeLine[i]:
                    markColon = True
            elif ' ' != CodeLine[i]:
                if '\t' != CodeLine[i]:
#                    print '? ',CodeLine[i]
                    return False
        if i < k - 1:
            sTemp = CodeLine[i:i+2]
            if '*/' == sTemp:
                markRemark = False
                i = i + 1
    return True

# 获取一行和初始查找位置，返输出该行假如找到if
#found = 0：符合if的开始条件。（' ', ';', '\t', '('）
#found = 1：不符合if的开始条件。
# done
# 通过了初步测试
