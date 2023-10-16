from django.urls import path
from registration import views

urlpatterns = [
    # path('',views.attendence_sheet,name='attendence'),
    path('',views.sign_up,name='signup'),
    path('log',views.log_in,name='login')
]