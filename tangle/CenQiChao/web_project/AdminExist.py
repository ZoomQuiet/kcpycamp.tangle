from django.http import HttpResponse

def AdminExists(request):
    AdminID = request.session.get('aLoginID', None)
    if AdminID:
        return True
    else:
        return False
