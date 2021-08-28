from .models import CustomUser
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if not request.method == 'GET':
        return JsonResponse({'error':'Send only get request'})
    try:
        username = request.GET['username']
        email = request.GET['email']
    except:
        return JsonResponse({"error":"Not found username or email field"})

    if CustomUser.objects.filter(email=email):
        return JsonResponse({"error":"Email already exists"})
    else:
        instance = CustomUser.objects.create(email=email,name=username)
        instance.save();
        return JsonResponse({"Success":"Successfully registered the user"});
        