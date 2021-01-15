from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import Transaction_detail_Serializer, user_monthly_detail_Serializer
from django.views.decorators.csrf import csrf_exempt
from .models import Bank_details, Transaction_detail, user_monthly_details

from django.shortcuts import render


# Create your views here.
@csrf_exempt
def Transaction_list(request):
    if request.method == 'GET':
        transaction = Transaction_detail.objects.all()
        serializer = Transaction_detail_Serializer(transaction, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Transaction_detail_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data['name_from'] == serializer.data['name_to']:
                return JsonResponse({'msg': 'not possible'}, status=400)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def User_Monthly_list(request):
    if request.method == 'GET':
        user_detail = user_monthly_details.objects.all()
        serializer = user_monthly_detail_Serializer(user_detail, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = user_monthly_detail_Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            if serializer.data['name'] == 'Null':
                return JsonResponse({'msg': 'not found the user,please enter correct username and try again'},
                                    status=400)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
