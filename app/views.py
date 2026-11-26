from django.shortcuts import render
from django.views.generic import View
import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class JSONApiView(View):
    def dispatch(self, request, *args, **kwargs):
        try:
            if request.method == 'POST':
                request.data = json.loads(request.body)
        except Exception as e:
            print(e) 
        return super().dispatch(request, *args, **kwargs)

class BmiView(JSONApiView):
    def post(self,request):
        data = request.data
        weight = data.get('weight')
        height = data.get('height')
        height = (height/100)**2
        return JsonResponse({
            'height':data.get('height'),
            'weight':weight,
            'BMI':round((weight/height),2)
            })
    
    

class AgeView(JSONApiView):
    def post(self,request):
        data = request.data
        current_year = data.get('current_year')
        birth_year = data.get('birth_year')
        age = current_year - birth_year
        return JsonResponse({
            'age':int(age)
        })


class PercentageView(JSONApiView):
    def post(self,request):
        data = request.data
        obtained_mark = data.get('obtained_mark')
        total_mark = data.get('total_mark')
        percentage = (obtained_mark/total_mark)*100
        return JsonResponse({
            'percentage':percentage
        })


class SimpleInterestView(JSONApiView):
    def post(self,request):
        data = request.data
        principal = data.get('principal')
        rate = data.get('rate')
        time = data.get('time')
        simpleinterest = (principal*rate*time)/100
        return JsonResponse({

            'si':simpleinterest
        })

class ElectricityBillView(JSONApiView):
    def post(self,request):
        data = request.data
        units = data.get('units')
        rate = data.get('rate')
        return JsonResponse({
            'price':units*rate
        })




class DiscountView(JSONApiView):
    def post(self,request):
        data = request.data
        price = data.get('price')
        discount_percentage = data.get('discount_percentage')
        discount = price *(discount_percentage/100)
        result = {
            'price':price,
            'discount_percentage':discount_percentage,
            'discount_amount': discount,
            "final_amouount": price- discount
        }
        return JsonResponse(result)



class ProfitCalculatorView(JSONApiView):
    def post(self,request):
        data = request.data
        cost_price = data.get('cost_price')
        selling_price = data.get('selling_price')
        profit =  selling_price - cost_price
        result = {
            'cost_price': cost_price , 
            'selling_price': selling_price , 
            'profit': profit
        }
        return JsonResponse(result)
    


class SalaryCalculatorView(JSONApiView):
    def post(self,request):
        data = request.data
        basic_salary = data.get('basic_salary')
        bonus = data.get('bonus')
        deduction = data.get('deduction')
        result = {
        "basic_salary": basic_salary,
        "bonus": bonus,
        "deduction": deduction,
        "net_salary": basic_salary+bonus - deduction
        }
        return JsonResponse(result)


class TimeConverterView(JSONApiView):
    def post(self, request):
        data = request.data
        hours = data.get('hours')
        return JsonResponse({
            'hours': hours,
            'minutes': hours * 60,
            'seconds': hours * 3600
        })


class FuelCostCalculatorView(JSONApiView):
    def post(self, request):
        data = request.data
        distance = data.get('distance')
        mileage = data.get('mileage')
        fuel_price = data.get('fuel_price')
        fuel_required = distance / mileage
        total_cost = fuel_required * fuel_price
        return JsonResponse({
            'distance': distance,
            'mileage': mileage,
            'fuel_price': fuel_price,
            'fuel_required': fuel_required,
            'total_cost': total_cost
        })



class ProductProfitCalculatorView(JSONApiView):
    def post(self, request):
        data = request.data
        cost_price = data.get('cost_price')
        selling_price = data.get('selling_price')
        quantity = data.get('quantity')
        total_cost = cost_price * quantity
        total_sales = selling_price * quantity
        profit = total_sales - total_cost
        result = {
            'cost_price': cost_price,
            'selling_price': selling_price,
            'quantity': quantity,
            'total_cost': total_cost,
            'total_sales': total_sales,
            'profit': profit
        }
        return JsonResponse(result)



class WorkSalaryCalculatorView(JSONApiView):
    def post(self, request):
        data = request.data

        hours_worked = data.get('hours_worked')
        regular_hours = data.get('regular_hours')
        hourly_rate = data.get('hourly_rate')
        overtime_rate = data.get('overtime_rate')
        regular_pay = regular_hours * hourly_rate
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * overtime_rate
        total_salary = regular_pay + overtime_pay
        result = {
            'hours_worked': hours_worked,
            'regular_hours': regular_hours,
            'hourly_rate': hourly_rate,
            'overtime_rate': overtime_rate,
            'regular_pay': regular_pay,
            'overtime_hours': overtime_hours,
            'overtime_pay': overtime_pay,
            'total_salary': total_salary
        }
        return JsonResponse(result)



class AgeDetailsView(JSONApiView):
    def post(self, request):
        data = request.data
        age = data.get('age')
        return JsonResponse({
            'age': age,
            'months': age * 12,
            'weeks': age * 52,
            'days': age * 365
        })