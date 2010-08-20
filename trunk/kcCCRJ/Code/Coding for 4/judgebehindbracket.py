# coding: UTF-8
#!/usr/bin/python
# Filename: JudgeBehindBracket.py

"""
@author: 方正圆
@license: kcCCRJ
@version：1.0
@tag：判断if,switch,while的()后是否有注释，空格以外的东西

@param CodeLine：需检测的字符串 
@type CodeLine: 字符串
@param Start: 从该行字符串的第几个位置开始检测
@type Start: 整型
@return: 若有注释，空格以外的东西则返回False，否则返回True
@rtype : bool
"""

def judgebehindbracket(line, i):
    judge = True
    remark = False
#    print '''len(line)''', len(line)
#    print '''i''',i
#    print line[i:len(line)]
    while i < len(line) - 1:
        i = i + 1
#        print '''line[i]:''', line[i]
#            print line[i:i+2]
           # print line[i]
           # print line[i+1]
        if ' ' == line[i]:
            continue
        if '\t' == line[i]:
            continue
        if '\n' == line[i]:
            continue
        if ';' == line[i]:
            continue
        
        if i < len(line) - 1:
            if '/' == line[i]:
                if '/' == line[i+1]:
#                    print '?'
                    break
            if '/' == line[i]:
                if '*' == line[i+1]:
                    remark = True

        if False == remark:
           # print '''line[i:len(line)]:''',line[i:len(line)]
            judge = False
            break
        
        if i < len(line) - 1:
            if '*' == line[i]:
                if '/' == line[i+1]:
                    remark = False
                    i = i + 1
                    
    return judge                    
