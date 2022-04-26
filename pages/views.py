from dataclasses import fields
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, FormView, View, UpdateView
from .forms import SupportForm, ContactForm
from django.urls import reverse_lazy
from .models import UserProfile
from django.shortcuts import render, redirect
from django.template.response import TemplateResponse

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
    
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        print(profile.user)
        user = profile.user
        followers = profile.followers.all()
        
        if len(followers) == 0:
            is_following = False
            
        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)
        context = {
            'user': user,
            'profile': profile,
            'is_following': is_following,
            'number_of_followers': number_of_followers,
        }
        return render(request, 'profile.html', context)

class AddFollower(LoginRequiredMixin, View):
    
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('profile', pk=profile.pk)

class RemoveFollower(LoginRequiredMixin, View):
    
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)

class ProfileEditView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model= UserProfile
    fields = ['name', 'bio', 'birth_date', 'location', 'picture']
    template_name = 'profile-edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

