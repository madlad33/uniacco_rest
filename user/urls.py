from django.urls import path,include
from .views import CreateUserView,CreateTokenView,CreateUserDetailView,UserDetailView
urlpatterns = [
path('create/',CreateUserView.as_view(),name='create'),
path('token/',CreateTokenView.as_view(),name='token'),
path('createdetail/',CreateUserDetailView.as_view(),name='create-detail'),
path('showdetail/',UserDetailView.as_view(),name='show-detail'),
]
