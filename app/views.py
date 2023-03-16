from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'condtional.html',d)
def loop(request):
    d={'name':'meghana'}
    return render(request,'loops.html',d)
