from rest_framework.views import APIView

from ide.models import Languages
from contest.models import Testcases, Problem, Contests
from ide.serializers import LanguageSerializer
from middleware.response import JSONResponse
import requests,traceback


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
        try:
            language_code = request.data['language_code'],
            contest_code = request.data['contest_code'],
            problem_code = request.data['problem_code'],
            code = request.data['code']

            language_code = str(language_code[0])
            contest_code = str(contest_code[0])
            problem_code = str(problem_code[0])

            key = 'hackerrank|1477209-1439|5df27efb8aaee3f89aaa2cfd77a809f0c9fd941b'
            url = 'http://api.hackerrank.com/checker/submission.json'
            payload = {}
            payload['source'] = code
            payload['api_key'] = key
            payload['format'] = 'json'
            payload['lang'] = language_code

            contest = Contests.objects.get(contest_code=contest_code)
            contest_id = contest.id
            problem = Problem.objects.filter(problem_code=str(problem_code),contest_id=str(contest_id))
            problem_id = problem.first().id
            test_cases = str(Testcases.objects.filter(problem_id=problem_id).values_list('input', flat=True))[10:-1]
            payload['test_cases'] = test_cases
            print payload
            response = requests.post(url, payload)
            print response.json()

            return JSONResponse({'HI':'hi'})

        except Exception as e:
            traceback_string = traceback.format_exc()
            response = {
                'message': 'Failed to Submit',
                'status': False,
                'exception': e.message
            }

            return JSONResponse(response)
