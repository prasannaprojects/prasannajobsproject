from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'testapp/index.html')


def Hydjobs(request):
   jobs_list = Hydjobs.objects.order_by('date')
   my_dict = {'jobs_list': jobs_list}
   return render(request, 'testapp/hydjobs.html', context=my_dict)

def Blorejobs(request):
   jobs_list = Blorejobs.objects.order_by('date')
   my_dict = {'jobs_list': jobs_list}
   return render(request, 'testapp/Blorejobs.html', context=my_dict)
