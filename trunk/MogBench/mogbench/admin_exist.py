#coding: utf-8	
'''检测用户是否已登录'''

from django.http import HttpResponse

def AdminExists(request):
    '''检测用户是否已登录'''
    AdminID = request.session.get('aLoginID', None)
    if AdminID:
        return True
    else:
        return False

        
if __name__ == "__main__":
    AdminExists(None)