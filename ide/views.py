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
            test_cases = Testcases.objects.filter(problem_id=problem_id).values_list("input", flat=True)
            test_cases = [tc.encode('ascii', 'ignore') for tc in test_cases]

            payload['testcases'] = str(test_cases)
            response = requests.post(url, payload)

            response = response.json()
            output = list(response['result']['stdout'])
            memory = response['result']['memory']
            total_memory = sum(memory)
            time = response['result']['time']
            total_time = sum(time)
            message = response['result']['message']
            compile_message = response['result']['compilemessage']
            status = ""
            if compile_message == "":
                if "Runtime error" in message:
                    status = "Runtime error"
                if "Terminated due to timeout" in message:
                    status = "TLE"
                correct_output = list(Testcases.objects.filter(problem_id=problem_id).values_list("output", "marks"))
                score = 0
                is_correct = True
                for i in range(len(correct_output)):
                    if output[i].strip() == correct_output[i][0]:
                        score += correct_output[i][1]
                    else:
                        is_correct = False

                if not status:
                    if is_correct:
                        status = "AC"
                    else:
                        status = "WA"
            else:
                status = "Compilation Error"
            response = {
                "Submission Status": status,
                "Time": total_time,
                "Memory": total_memory,
                "Score": score,
                "Compile Message": compile_message
            }

            return JSONResponse(response)

        except Exception as e:
            traceback_string = traceback.format_exc()
            response = {
                'message': 'Failed to Submit',
                'status': False,
                'exception': e.message
            }

            return JSONResponse(response)
