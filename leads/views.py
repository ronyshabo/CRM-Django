from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead
def Lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render( request, 'leads/lead_list.html',context)

def secondpage(request):

    return render( request, 'secondpage.html')

def lead_detail(request,pk):
    print(pk)
    lead= Lead.objects.get(id=pk)
    print(lead)
    return HttpResponse("here is the detailed view")