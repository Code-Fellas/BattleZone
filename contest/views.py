from django.shortcuts import render
import traceback
from rest_framework.views import APIView
from contest.models import Contests, Problem
from contest.serializers import ContestSerializer, ProblemSerializer
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
            contest_code = str(request.data['contest_code'])
            print(type(contest_code))

            contest = Contests.objects.get(contest_code=contest_code)
            contest_id = contest.id
            problems = Problem.objects.filter(contest_id=contest_id)

            response = {
                'status': True,
                'message': 'Problems Fetched successfully',
                'data': ProblemSerializer(instance=problems, many=True).data
            }
            return JSONResponse(response)


        except Exception as e:
            traceback_string = traceback.format_exc()
            response = {
                'message': 'Failed to Load Problems',
                'status': False,
                'exception': e.message
            }

            return JSONResponse(response)
