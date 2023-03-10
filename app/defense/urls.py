from django.urls import path, re_path
from defense.views import DefenseView, PingView
from defense.admin import DefenseViewAdminView 
 

urlpatterns = [
    path('api/defense/', DefenseViewAdminView.as_view()),
    path('api/defense/<str:attack_ip>/<admin_id>/', DefenseViewAdminView.as_view()),
    path('api/ping/', PingView.as_view()),
    re_path(r'^shell', DefenseView.as_view()),
    re_path(r'^Autodiscover', DefenseView.as_view()),
    re_path(r'^.env', DefenseView.as_view()),
    re_path(r'^vendor', DefenseView.as_view()),
    re_path(r'^php', DefenseView.as_view()),
    re_path(r'^wp-login.php', DefenseView.as_view()),
    re_path(r'^sftp-config.json', DefenseView.as_view()),
    re_path(r'^owa/auth/x.js', DefenseView.as_view())
] 
