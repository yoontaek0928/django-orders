from django.shortcuts import render
from user.models import User
from user.serializers import UserSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.utils import timezone

# @csrf_exempt
# def user(request):
#     if request.method == 'GET':
#         user = User.objects.all()