from django.shortcuts import render
import traceback
from rest_framework.views import APIView
from contest.models import Contests
from contest.serializers import ContestSerializer
from middleware.response import JSONResponse


# Create your views here.

class FetchContestsView(APIView):

    def get(self, request):

        response = {
            'status': True,
            'message': 'Contests Fetched successfully',
            'data' : ContestSerializer(instance=Contests.objects.all(), many=True).data
        }
        return JSONResponse(response)


class FetchProblemsView(APIView):

    def post(self, request):
        try:
            contest_code = request.data['contest_code']
            print(contest_code)


        except Exception as e:
            traceback_string = traceback.format_exc()
            response = {
                'message': 'Failed to Load Problems',
                'status': False,
                'exception': e.message
            }

            return JSONResponse(response)
