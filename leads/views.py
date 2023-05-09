from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead,Agent
from .forms import LeadForm,LeadModelForm
# With the TemplateView class. we can add all 4 CRUD methods to this class. eg: UpdateView
from django.views.generic import TemplateView, ListView, DetailView

import logging

logging.basicConfig(
    filename="logs/views.log",
    level=logging.DEBUG,
    format="%(module)s : %(levelname)s:  %(message)s - : %(asctime)s",
)


class LandingPageView(TemplateView):
    template_name="landing.html"
    

def landing_page(request):
     return render( request, 'landing.html')


class LeadListView(ListView):
    template_name = " leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"
    
def Lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render( request, 'leads/lead_list.html',context)

class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

def lead_detail(request,pk):
    lead= Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render( request, 'leads/lead_detail.html',context)

def lead_create(request):
    logging.info("reaching the lead create func")
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        logging.info(f"Post request format is : {request.POST}")
        if form.is_valid():
            form.save()
        #This line replaces all those
            # logging.info(f"the cleaned data: {form.cleaned_data}")
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # age = form.cleaned_data['age']
            # agent = form.cleaned_data['agent']
            # Lead.objects.create(
            #     first_name=first_name,
            #     last_name=last_name,
            #     age=age,
            #     agent=agent
            # )
            return redirect('/leads')
        else:
            logging.warning("Form is not valid")

           
    context = {
        "form": LeadModelForm()
    }
    return render( request, 'leads/lead_create.html',context)

def lead_update(request,pk):
    lead= Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST,instance=lead)
        if form.is_valid():
            logging.info(f"the cleaned data: {form.cleaned_data}")
            lead.save()
            return redirect('/leads')
    context = {
        "form": form,
        "lead": lead
    }
    return render( request, 'leads/lead_update.html',context)

def lead_delete(request,pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('/leads')



def secondpage(request):

    return render( request, 'secondpage.html')