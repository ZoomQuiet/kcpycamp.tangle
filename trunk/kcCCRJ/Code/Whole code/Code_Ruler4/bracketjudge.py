# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: BracketJudge.py
"""
@author: ����Բ
@license: kcCCRJ
@version��1.0
@tag���ж��ַ���ĳ��λ�ú�����������Ƿ�ƥ�䣬��ƥ�䷵��ֵf=True������f=false��ɨ����Ϣ��ΪԪ�鷵�ء�

@param CodeLine��������ַ��� 
@type CodeLine: �ַ���
@param left: �������Ѿ��ж��ٸ�
@type left: ����
@param right: �������Ѿ��ж��ٸ�
@type right: ����
@param start: ���ַ������ĸ�λ�ÿ�ʼɨ��
@type start: ����
@return left:��������Ŀ
@rtype left: ����
@return right: ��������Ŀ
@rtype right: ����
@return f: ��ǰ���������Ƿ�ƥ��
@rtype f: bool
@return place: ��ƥ�䣬place����ƥ�䵽�����һ�������ŵ�λ��
@rtype right: ����
"""
def bracketjudge(CodeLine, left, right, start):
    i = start
    f = False
    place = 0
    while i < len(CodeLine):
        if '(' == CodeLine[i]:#��������ƥ��
            left = left + 1
        elif ')' == CodeLine[i]:
            right = right + 1
        i = i + 1
        if 0 < left:
            if left == right:#����ɨ����һ�������ţ��ҵ�ǰ����������ƥ��
                f = True
                place = i
                break
    return (left, right, f, place)
