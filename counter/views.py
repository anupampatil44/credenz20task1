from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import RequestContext

n=[]

def home(request):
    return render(request,'counter/counter.html',{'n':n})
def nos(request):
    if request.method=="POST":
        n=[]
        start=int(request.POST.get("start"))
        end=int(request.POST.get("end"))


        if start<end:
            for i in range(start,end+1):
                n.append(i)
        return render(request,'counter/counter.html',{'n':n})