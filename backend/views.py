# backend/views.py
from django.http import JsonResponse

def example_api_view(request):
    data = {
        'message': 'Hello, this is data from the backend!'
    }
    return JsonResponse(data)
