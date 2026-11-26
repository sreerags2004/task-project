"""
URL configuration for task_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bmi/',views.BmiView.as_view()),
    path('age/',views.AgeView.as_view()) , 
    path('percentage/',views.PercentageView.as_view()), 
    path('simple_interest/',views.SimpleInterestView.as_view()),
    path('electricity_bill/',views.ElectricityBillView.as_view()) , 
    path('discount/',views.DiscountView.as_view()) , 
    path('profit/',views.ProfitCalculatorView.as_view()) , 
    path('salary/',views.SalaryCalculatorView.as_view()) , 
    path('time/', views.TimeConverterView.as_view()),
    path('fuel_cost/', views.FuelCostCalculatorView.as_view()),
    path('product_profit/', views.ProductProfitCalculatorView.as_view()),
    path('work_salary/', views.WorkSalaryCalculatorView.as_view()),
    path('age_details/', views.AgeDetailsView.as_view()),

]
