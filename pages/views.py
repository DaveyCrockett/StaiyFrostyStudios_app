from django.views.generic import TemplateView, FormView
from .forms import SupportForm, ContactForm
from django.urls import reverse_lazy

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"
    
class AboutPageView(TemplateView):
    template_name = "about.html"

class SupportPageView(FormView):
    template_name = 'support.html'
    form_class = SupportForm
    success_url = reverse_lazy('support-success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

class SupportSuccessView(TemplateView):
    template_name = 'support-success.html'

class ContactPageView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'contact-success.html'

class ProfilePageView(TemplateView):
    template_name = 'profile.html'