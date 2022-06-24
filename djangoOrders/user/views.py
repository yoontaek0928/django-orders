from django.shortcuts import render
from user.models import User
from user.serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone

@csrf_exempt
def user(request):
    if request.method == 'GET':
        user = User.objects.all()
        return render(request, 'user/user_list.html',{'user_list':user})
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)