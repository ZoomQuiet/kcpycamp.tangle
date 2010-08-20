from django.shortcuts import render_to_response

list = [{'id':'0001', 'name':'kkkkkk', 'mark':'70'}]

def showmap(request):
    return render_to_response('kcstu.html', {'list': list})
