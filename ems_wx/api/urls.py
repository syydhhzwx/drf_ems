from django.urls import path

from api import views

urlpatterns = [
    path('users/', views.UserAPIView.as_view()),
    path('employeess/', views.EmployeesAPIView.as_view()),
    path('employeess/<id>/', views.EmployeesAPIView.as_view()),

]
