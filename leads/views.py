from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm, LeadModelForm

def Lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render( request, 'leads/lead_list.html',context)

def secondpage(request):

    return render( request, 'secondpage.html')

def lead_detail(request,pk):
    lead= Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render( request, 'leads/lead_detail.html',context)

def lead_create(request):
    print("reaching the lead create func")
    print(request.POST)
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            print(f"the cleaned data: {form.cleaned_data}")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                first_name=first_name,
                last_name=last_name,
                age=age,
                agent=agent
            )
            return redirect('/leads')
    context = {
        "form": LeadForm()
    }
    return render( request, 'leads/lead_create.html',context)