from distutils.command.config import config
from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView, ContactSuccessView, SupportPageView, SupportSuccessView, ProfilePageView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('support/', SupportPageView.as_view(), name='support'),
    path('support-success/', SupportSuccessView.as_view(), name="support-success"),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('contact-success/', ContactSuccessView.as_view(), name="contact-success"),
    path('profile/<int:pk>', ProfilePageView.as_view(), name='profile'),
] 