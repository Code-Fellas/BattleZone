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
            d = {}
            d['source'] = code
            d['api_key'] = key
            d['format'] = 'json'
            d['lang'] = language_code

            contest = Contests.objects.get(contest_code=contest_code)
            contest_id = contest.id
            problem = Problem.objects.filter(problem_code=str(problem_code),contest_id=str(contest_id))
            problem_id = problem.first().id
            test_cases = Testcases.objects.filter(problem_id=problem_id)


            for test_case in test_cases:
                d['testcases'] = str(test_case.input)
                print d['testcases']
                re = requests.post(url, data=d)
                print re.json()

            return JSONResponse({'HI':'hi'})

        except Exception as e:
            traceback_string = traceback.format_exc()
            response = {
                'message': 'Failed to Submit',
                'status': False,
                'exception': e.message
            }

            return JSONResponse(response)
