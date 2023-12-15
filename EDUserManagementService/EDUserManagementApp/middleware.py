from django.http import JsonResponse
from EDUserManagementApp.models import ServiceAccount  # Adjust the import according to your model location

def token_auth_middleware(get_response):
    def middleware(request):
        token = request.headers.get('Authorization')
        if not ServiceAccount.objects.filter(token=token).exists():
            return JsonResponse({'error': 'Unauthorized'}, status=401)
        return get_response(request)

    return middleware
