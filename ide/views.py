from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from ide.models import Languages
from django.contrib.auth.hashers import make_password
from middleware.response import JSONResponse
from ide.serializers import LanguageSerializer
import traceback

# Create your views here.


class FetchLanguagesView(APIView):

    def get(self, request):

        response = {
            'status': True,
            'message': 'Languages Fetched successfully',
            'data' : LanguageSerializer(instance=Languages.objects.all(), many=True).data
        }
        return JSONResponse(response)


class SubmissionView(APIView):

    def post(self, request):
        pass
