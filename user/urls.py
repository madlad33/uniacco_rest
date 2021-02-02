from django.urls import path,include
from .views import CreateUserView,CreateTokenView
urlpatterns = [
path('create/',CreateUserView.as_view(),name='create'),
path('token/',CreateTokenView.as_view(),name='token'),

]
