from django.shortcuts import render

# Create your views here.
def oldmonk(request):
    return render(request,'oldmonk.html')

def redlabel(request):
    return render(request,'redlabel.html')