from django.shortcuts import render
from .models import ProductModel
from django.http import JsonResponse
# Create your views here.

def all_products(request):
    all = ProductModel.objects.all()
    results = list(all.values())
    return JsonResponse({'products':results})