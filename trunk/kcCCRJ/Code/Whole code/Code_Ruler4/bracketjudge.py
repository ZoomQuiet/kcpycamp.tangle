# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: BracketJudge.py
"""
@author: 方正圆
@license: kcCCRJ
@version：1.0
@tag：判定字符串某个位置后的左右括号是否匹配，若匹配返回值f=True，否则f=false。扫描信息作为元组返回。

@param CodeLine：需检测的字符串 
@type CodeLine: 字符串
@param left: 左括号已经有多少个
@type left: 整型
@param right: 右括号已经有多少个
@type right: 整型
@param start: 从字符串的哪个位置开始扫描
@type start: 整型
@return left:左括号数目
@rtype left: 整型
@return right: 右括号数目
@rtype right: 整型
@return f: 当前左右括号是否匹配
@rtype f: bool
@return place: 若匹配，place等于匹配到的最后一个右括号的位置
@rtype right: 整型
"""
def bracketjudge(CodeLine, left, right, start):
    i = start
    f = False
    place = 0
    while i < len(CodeLine):
        if '(' == CodeLine[i]:#左右括号匹配
            left = left + 1
        elif ')' == CodeLine[i]:
            right = right + 1
        i = i + 1
        if 0 < left:
            if left == right:#至少扫描了一个左括号，且当前左右括号能匹配
                f = True
                place = i
                break
    return (left, right, f, place)
