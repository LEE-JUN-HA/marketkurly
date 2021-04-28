import json
import bcrypt
import jwt

from django.views import View
from django.http  import JsonResponse

from my_settings  import SECRET_KEY, ALGORITHM
from .utils       import login_decorator
from .models      import User

class SigninView(View):
    def post(self, request):
        try: 
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            user     = User.objects.get(email=email)
            token    = jwt.encode({'user_id': user.id}, SECRET_KEY, ALGORITHM)

            if not User.objects.filter(email = email).exists():
                return JsonResponse({'mesage' : 'INVALID_USER'}, status = 401)

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message': 'SUCCESS', 'access_token': token}, status=200)
            return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)

