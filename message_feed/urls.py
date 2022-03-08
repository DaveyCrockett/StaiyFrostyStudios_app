from django.urls import path
from .views import MessageCreateView, MessageDeleteView, MessageDetailView, MessageListView, MessageUpdateView



urlpatterns = [
    path('', MessageListView.as_view(), name='messages'),
    path('message_detail/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('new_message/', MessageCreateView.as_view(), name='new_message'),
    path('edit_message/<int:pk>', MessageUpdateView.as_view(), name='edit_message'),
    path('delete_message/<int:pk>', MessageDeleteView.as_view(), name='delete_message'),
] 