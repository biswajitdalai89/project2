from django.shortcuts import render

# Create your views here.
def biriyani(request):
    return render(request,'biriyani.html')

def gulabjamun(request):
    return render(request,'gulabjamun.html')