from django.shortcuts import render
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

@csrf_exempt
def shop(request):
    if request.method == 'GET':
        shop = Shop.objects.all()   # shop 데이터 베이스에 있는 모든 object는 모두 shop에 저장
        serializer = ShopSerializer(shop, many=True)    # 그 데이터들은 모두 serializer를 통해 json 형태로 파싱
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)  # 데이터를 json 형태로 바꿔주기
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
        