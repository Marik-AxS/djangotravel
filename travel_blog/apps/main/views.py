from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView
from .models import AboutUs, Contacts
from .forms import ContactUsForm
# Create your views here

class HomeView(TemplateView):
    template_name = 'pages/index.html'

class AboutUsView(TemplateView):
    template_name = 'pages/about_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUs.objects.first()
        return context

class ContactUsView(CreateView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.first()
        return context

# class ContactsView(TemplateView):
#     template_name = 'pages/contact_us.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['contacts'] = Contacts.objects.first()
#         return context
