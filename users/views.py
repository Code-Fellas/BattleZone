import traceback

from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from middleware.response import JSONResponse
from users.models import Users, Tokens
from users.serializers import UserSerializer


# Create your views here.


class UserCreateView(APIView):

    def post(self, request):
        try:
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email_id = str(request.data['email']).strip()
            mobile_number = request.data['mobile_number']
            academic_year = int(request.data['academic_year'])
            password = make_password(request.data['password'])
            username = str(request.data['username'])
            university = request.data['university']

            user_object = Users.objects.filter(email=email_id)
            if user_object.exists():
                current_user = user_object.first()
                if not current_user.is_active :
                    current_user.is_active = True
                    current_user.save()
                    response = {
                        'status': True,
                        'message': 'User is now active'
                    }
                else:
                    response = {
                        'status': False,
                        'message': 'User already exists',
                    }
                return JSONResponse(response)

            else:
                new_user = Users.objects.create(
                                first_name=first_name,
                                last_name=last_name,
                                email=email_id,
                                username=username,
                                password=password,
                                mobile_number=mobile_number,
                                current_year=academic_year,
                                current_university=university,
                                is_active=True,
                            )

                return JSONResponse({
                    'status': True,
                    'message': 'User Created Successfully',
                    'result': UserSerializer(instance=new_user).data
                })

        except Exception as e:
            traceback_string = traceback.format_exc()

            response = {
                'message': 'Failed to Create New User',
                'status': False,
                'exception': e.message
            }

            return JSONResponse(response)


class UserLoginView(APIView):

    def post(self, request):
        try:
            username = request.data["username"]
            password = request.data["password"]
        except KeyError:
            return JSONResponse({"error_message": "Username or Password not provided! Invalid Request."}, status=400)
        user = Users.objects.filter(username=username).first()

        if user is None:
            return JSONResponse({"error_message": "Invalid Username or Password."}, status=400)
        if not check_password(password, user.password):
            return JSONResponse({"error_message": "Invalid Username or Password."}, status=400)

        access_token = Tokens(user_id=user)
        access_token.create_token()
        access_token.save()

        return JSONResponse({"access_token": access_token.access_token}, status=200)


def check_token(request):
    try:
        access_token = request.META['HTTP_TOKEN']
    except KeyError:
        return 'KeyError'

    token_exists = Tokens.objects.filter(access_token=access_token, is_valid=True).first()

    if not token_exists:
        return None

    return token_exists.user_id


class UserLogoutView(APIView):

    def post(self, request):
        current_user = check_token(request)

        if current_user is None:
            return JSONResponse({"error_message": "Invalid Access Token."}, status=400)

        if current_user == 'KeyError':
            return JSONResponse({"error_message": "Access Token not found in Header.Please pass it as 'token'"}, status=400)

        access_token = request.META['HTTP_TOKEN']
        cur_token = Tokens.objects.filter(access_token=access_token).first()
        cur_token.is_valid = 0
        cur_token.save()

        return JSONResponse({"success": "User Logged Out."}, status=200)
