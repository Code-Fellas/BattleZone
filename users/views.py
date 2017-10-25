from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import Users
from django.contrib.auth.hashers import make_password
from middleware.response import JSONResponse
from users.serializers import UserSerializer
import traceback

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