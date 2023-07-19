from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from agents.mixins import OrganisorAndLoginRequiredMixin
from django.http import HttpResponse
from .models import Lead,Agent, Category
from .forms import LeadForm,LeadModelForm, CustomUserCreationForm, AssignAgentForm
# With the TemplateView class. we can add all 4 CRUD methods to this class. eg: UpdateView
from django.views import generic

import logging

logging.basicConfig(
    filename="logs/views.log",
    level=logging.DEBUG,
    format="%(module)s : %(levelname)s:  %(message)s - : %(asctime)s",
)

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect("dashboard")
    #     return super().dispatch(request, *args, **kwargs)
    

# def landing_page(request):
#      return render( request, 'landing.html')


class LeadListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/lead_list.html"
    context_object_name = "leads"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation=user.userprofile, 
                agent__isnull=False
            )
        else:
            queryset = Lead.objects.filter(
                # organisation=user.agent.organisation, 
                agent__isnull=False
            )
            # filter for the agent that is logged in
            queryset = queryset.filter(agent__user=user)
        return queryset

    def get_context_data(self,**kwargs):
        '''
        This function helps devide the leads into 2 groups, leads with agents. and leads without agents that are ready to be assigned
        '''
        user = self.request.user
        context = super(LeadListView, self).get_context_data(**kwargs)
        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation=user.userprofile,
                agent__isnull=True
                )
            context.update({
                "unassigned_leads":queryset
            })
        return context
    
    
# def Lead_list(request):
    # leads = Lead.objects.all()
    # context = {
    #     "leads": leads
    # }
    # return render( request, 'leads/lead_list.html',context)

class LeadDetailView(LoginRequiredMixin,generic.DetailView):
    template_name = "leads/lead_detail.html"
    context_object_name = "lead"

    def get_queryset(self):
        user = self.request.user
        if user.is_organisor:
            queryset = Lead.objects.filter(organisation=user.userprofile)
        else:
            queryset = Lead.objects.filter(organisation=user.agent.organisation)
            queryset = queryset.filter(agent__user=user)
        return queryset

# def lead_detail(request,pk):
    # lead= Lead.objects.get(id=pk)
    # context = {
    #     "lead": lead
    # }
    # return render( request, 'leads/lead_detail.html',context)

class LeadCreateView(OrganisorAndLoginRequiredMixin,generic.CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse('leads:lead-list')

    def form_valid(self, form):
        # TODO send email
        send_mail(
            subject="A lead has been created",
            message="Visit the site to confirm",
            from_email="test@test.com",
            recipient_list=["test2@test.com"]
        )
        return super (LeadCreateView, self).form_valid(form)

# def lead_create(request):
    # logging.info("reaching the lead create func")
    # form = LeadModelForm()
    # if request.method == "POST":
    #     form = LeadModelForm(request.POST)
    #     logging.info(f"Post request format is : {request.POST}")
    #     if form.is_valid():
    #         form.save()
    #     #This line replaces all those
    #         # logging.info(f"the cleaned data: {form.cleaned_data}")
    #         # first_name = form.cleaned_data['first_name']
    #         # last_name = form.cleaned_data['last_name']
    #         # age = form.cleaned_data['age']
    #         # agent = form.cleaned_data['agent']
    #         # Lead.objects.create(
    #         #     first_name=first_name,
    #         #     last_name=last_name,
    #         #     age=age,
    #         #     agent=agent
    #         # )
    #         return redirect('/leads')
    #     else:
    #         logging.warning("Form is not valid")

           
    # context = {
    #     "form": LeadModelForm()
    # }
    # return render( request, 'leads/lead_create.html',context)


class LeadUpdateView(OrganisorAndLoginRequiredMixin,generic.UpdateView):
    template_name = "leads/lead_update.html"
    form_class = LeadModelForm

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse('leads:lead-list')


# def lead_update(request,pk):
    # lead= Lead.objects.get(id=pk)
    # form = LeadModelForm(instance=lead)
    # if request.method == "POST":
    #     form = LeadModelForm(request.POST,instance=lead)
    #     if form.is_valid():
    #         logging.info(f"the cleaned data: {form.cleaned_data}")
    #         lead.save()
    #         return redirect('/leads')
    # context = {
    #     "form": form,
    #     "lead": lead
    # }
    # return render( request, 'leads/lead_update.html',context)

class LeadDeleteView(OrganisorAndLoginRequiredMixin,generic.DeleteView):
    template_name = "leads/lead_delete.html"

    def get_queryset(self):
        user = self.request.user
        return Lead.objects.filter(organisation=user.userprofile)

    
    def get_success_url(self):
        return reverse('leads:lead-list')


    def lead_delete(request,pk):
        lead = Lead.objects.get(id=pk)
        lead.delete()
        return redirect('/leads') 

class AssignAgentView(OrganisorAndLoginRequiredMixin, generic.FormView):
    template_name = "leads/assign_agent.html"
    form_class = AssignAgentForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AssignAgentView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs
        
    def get_success_url(self):
        return reverse("leads:lead-list")

    def form_valid(self, form):
        agent = form.cleaned_data["agent"]
        lead = Lead.objects.get(id=self.kwargs["pk"])
        lead.agent = agent
        lead.save()
        return super(AssignAgentView, self).form_valid(form)

def secondpage(request):

    return render( request, 'secondpage.html')

class CategoryListView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/category_list.html"
    context_object_name = "category_list"

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        user = self.request.user

        if user.is_organisor:
            queryset = Lead.objects.filter(
                organisation=user.userprofile
            )
        else:
            queryset = Lead.objects.filter(
                organisation=user.agent.organisation
            )

        context.update({
            "unassigned_lead_count": queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Category.objects.filter(
                organisation=user.userprofile
            )
        else:
            queryset = Category.objects.filter(
                organisation=user.agent.organisation
            )
            queryset = queryset.filter(agent__user=user)
        return queryset
