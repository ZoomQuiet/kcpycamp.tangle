from django.shortcuts import render_to_response

list = [{'id':'0001', 'name':'张三', 'mark':'70'}]

def index(request):
    return render_to_response('kcear.html', {'list': list})
