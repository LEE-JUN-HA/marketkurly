from django.urls import path
from .views      import SigninView

urlpatterns = [
    path('/signin', SigninView.as_view()),
    path('/signup', SignupView.as_view()),
]