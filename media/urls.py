from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView

)
from . import views
import user.views as view

urlpatterns = [
    path('', PostListView.as_view(), name='media-home'),
    path('car/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('car/new/', PostCreateView.as_view(), name='post-create'),
    path('car/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('car/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='media-about'),
    path('inbox/', view.inbox, name="inbox"),
    path('message/<str:pk>/', view.viewMessage, name="message"),
    path('create-message/<str:username>/', view.createMessage, name="create-message"),

]
