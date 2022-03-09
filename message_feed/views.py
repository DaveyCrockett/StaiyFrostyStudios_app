from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Message
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class MessageListView(ListView):
    template_name = "message_list.html"
    model = Message

class MessageDetailView(DetailView):
    template_name = "message_detail.html"
    model = Message

class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = "new_message.html"
    model = Message
    fields = ["title", "body", "creator"]

class MessageUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    template_name = "edit_message.html"
    model = Message
    fields = ["title", "body"]

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user

class MessageDeleteView(LoginRequiredMixin , UserPassesTestMixin,DeleteView):
    template_name = "delete_message.html"
    model = Message
    success_url = reverse_lazy('messages')

    def test_func(self):
        obj = self.get_object()
        return obj.creator == self.request.user