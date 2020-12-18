from django.conf.urls import url
from .views import UserRegistrationView


urlpatterns = [
    url('signup', UserRegistrationView.as_view()),
    ]
