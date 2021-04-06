import json
import bcrypt
import jwt

from django.views import View
from django.http  import JsonResponse

from my_settings  import SECRET_KEY, ALGORITHM
from .utils       import login_decorator
from .models      import User

class SignupView(view):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            email          = data['email']
            password       = data['password']                                
            name           = data['name']
            password_regex = re.compile("(?=.*\d)(?=.*[a-z]).{8,32}$", re.IGNORECASE)
            email_regex    = re.compile("^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$")

            if not password_regex.match(password):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 400)

            if not email_regex.match(email):
                return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'message' : 'DUPLICATED_EMAIL'}, status = 400)

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                email        = email,
                password     = hashed_password,
                name         = name
            )
            return JsonResponse({'message' : 'SUCCESS'}, status = 201)
                
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
