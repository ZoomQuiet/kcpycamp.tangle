# -*- coding: cp936 -*-
# Filename: ccrj_main.py

def main(SrcFilename, DestFilename, Option):
    """���ø����жϺ�����������"""
    print "\n"
    print "\t���������ļ���%s."%SrcFilename
    if Option == "":
        print "\tĬ�����м�����е�����"
    else:
        print "\t����ѡ��������:%s."%Option
    print "\t��������"
    print "\t���,���������%s."%DestFilename
    
