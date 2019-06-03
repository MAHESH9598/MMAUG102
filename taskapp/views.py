from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'html1.html')

def add(request):
    operation=request.POST["op"]
    try:
        a = request.POST["n1"]
        b = request.POST["n2"]
        i = int(a)
        j = int(b)
    except(ValueError):
        return render(request, 'html1.html')
    if operation=="add":
        k = i + j
        return HttpResponse("""<html><body bgcolor=navy><center><br><br><h1><span style=background-color:yellow;>Result of SUM :"""+str(k)+"""</span></h1></center></body></html>""")
    elif operation=="sub":
        k = i - j
        return HttpResponse("""<html><body bgcolor=navy><center><br><br><h1><span style=background-color:yellow;>Result of SUM :"""+str(k)+"""</span></h1></center></body></html>""")
    elif operation=="mul":
        k = i * j
        return HttpResponse("""<html><body bgcolor=navy><center><br><br><h1><span style=background-color:yellow;>Result of SUM :"""+str(k)+"""</span></h1></center></body></html>""")
    elif operation=="div":
        try:
            k=i/j
            return HttpResponse("""<html><body bgcolor=navy><center><br><br><h1><span style=background-color:yellow;>Result of SUM :""" + str(k)+"""</span></h1></center></body></html>""")
        except(ZeroDivisionError):
            return render(request,'html1.html')



