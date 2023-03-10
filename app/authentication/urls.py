from django.urls import path
from .views import  LoginView, LogoutView, ProtectedView, Register


 
urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/<int:user_id>/', LogoutView.as_view()),
    path('delete-account/<int:user_id>/', ProtectedView.as_view()),
    path('change-password/', ProtectedView.as_view()),
]
 