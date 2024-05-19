from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder

def submit_expense(request):
    """user submit an expense"""

    print ("we are here")
    print(request.POST)

    return JsonResponse({
        'status' : 'ok',
    }, encoder=JSONEncoder)
