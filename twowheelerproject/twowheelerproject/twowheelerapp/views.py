from django.shortcuts import render
from.models import Place
from.models import Team
# Create your views here.
def home(request):
    object1 = Place.objects.all()
    object2 = Team.objects.all()

    context = {
        'object1': object1,
        'object2': object2
    }
    return  render(request,"index.html",context)

def index(request):
    return render(request,"index.html")


# def home(request):
#     obj=Team.objects.all()
#     return  render(request,"index.html",{'result1':obj})
#def addition(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
   # res=x+y
    #return  render(request,"result.html",{'result':res})