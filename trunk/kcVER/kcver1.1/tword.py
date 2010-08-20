# -*- coding: cp936 -*-
def Word2URL(word):
    bret = isinstance(word,unicode)
    #print bret
    #print len(word)
    word = unicode(word,'cp936')
    #print len(word)
    sret =u''
    for i in word:
        #print i,ord(i)
        if ord(i)<=127:
            b1 = i.isdigit()
            b2 = i.isalpha()
            #print b1,b2,i,(not b1 and not b2)
            if not b1 and not b2:
                pass
                if sret != u'' and sret[-1]!='-':
                    sret +=i.replace(i,'-')
            else:
                #if sret != u'' and sret[-1]!='-':
                sret +=i
        else:
            if sret != u'' and sret[-1]!='-':
                sret +=i.replace(i,'-')
                pass
    #print sret
    sret=sret.lower()
    sret = u'tag/'+sret
    if not sret.endswith('-'):
        sret+=u'-'
    bret = isinstance(sret,unicode)
    #print bret ,len(sret),sret
    sret1 = sret.encode('cp936')
    bret = isinstance(sret1,unicode)
    #print bret,len(sret1),sret1,sret1==sret
    return sret1
    pass

if __name__ == '__main__':
    #Word2URL('hao你123好')
    path = 'tag.txt'
    f = open(path,'r')
    lines = f.readlines()
    print len(lines)
    lisql=[]
    tid = 20009
    
    for i in lines:
        pos = i.find('\t')
        s1=i[0:pos].strip()
        s2=i[pos:-1].strip()
        sret=Word2URL(s1)
        print '[',s1,':',s2,']'
        print sret,s2.startswith(sret)
        
        lisql.append("insert into `url_alias` (`src`,`dst`) values ('%s','%s%s.html')"%(tid,sret,tid))
        q=lisql[lines.index(i)]
        q4=unicode(q,'cp932')
        print q
        print q4
        q0='python语言'
        b1=isinstance(q0,unicode)
        q1=unicode(q0,'cp936')
        b2=isinstance(q1,unicode)
        b3=isinstance(q,unicode)
        print b1,b2,b3
        print q1
        print '*'*40
        
    
    
    
