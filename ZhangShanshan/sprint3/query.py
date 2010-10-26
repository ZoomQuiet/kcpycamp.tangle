#query key words
def TokenTerms(word):
     sword = word.strip()
     li=sword.split(',')
     li=list(set(li))
     return li
def QueryTerm(term):
     pass
     
if __name__ == '__main__':
    while 1:
        s = raw_input('Enter word:')
        if s == 'q':
            break
        li = TokenTerms(s)
        for i in li:
            print i
    
