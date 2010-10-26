import ConfigParser
#import string, os, sys
cf = ConfigParser.ConfigParser()
cf.read('cfg.txt')
s=cf.sections()
print 'sec',s
v=cf.items('txt_field')
#print 'item',v

for t in v:
    print t[0],'[',t[1],']'

v=cf.items('db_field')
#print 'item',v

for t in v:
    print t[0],'[',t[1],']'


