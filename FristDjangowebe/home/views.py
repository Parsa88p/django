from django.shortcuts import render

# Create your views here.
def page1(request):
    return render(request,'home/page1.html')
def page2(requset):
    return render(requset,'page2.html')
