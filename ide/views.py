from rest_framework.views import APIView

from ide.models import Languages
from contest.models import Testcases, Problem, Contests
from ide.serializers import LanguageSerializer
from middleware.response import JSONResponse
import requests, traceback


# Create your views here.


class FetchLanguagesView(APIView):
    def get(self, request):
        response = {
            'status': True,
            'message': 'Languages Fetched successfully',
            'data': LanguageSerializer(instance=Languages.objects.all(), many=True).data
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
            problem = Problem.objects.filter(problem_code=str(problem_code), contest_id=str(contest_id))
            problem_id = problem.first().id
            test_cases = Testcases.objects.filter(problem_id=problem_id).values_list("input", flat=True)
            test_cases = [tc.encode('ascii', 'ignore') for tc in test_cases]

            payload['testcases'] = str(test_cases)
            response = requests.post(url, payload)

            response = response.json()
            if response['result']['stdout'] is not None:
                output = list(response['result']['stdout'])
            else:
                output = None
            memory = response['result']['memory']
            stderr = response['result']['stderr']
            time = response['result']['time']
            message = response['result']['message']
            compile_message = response['result']['compilemessage']
            score = 0
            response = {
                "Submission Status": None,
                "Time": None,
                "Memory": None,
                "Score": 0,
                "Compile Message": None
            }
            if compile_message != "":
                response["Submission Status"] = "CE"
                response["Compile Message"] = compile_message

            else:
                if "Terminated due to timeout" in message:
                    response["Submission Status"] = "TLE"
                if "Runtime Error" in message:
                    response["Submission Status"] = "RTE"

                response["TestCases"] = {"Errormessage": stderr, "Status": message}
                correct_output = list(Testcases.objects.filter(problem_id=problem_id).values_list("output", "marks"))
                for i in range(len(correct_output)):
                    if message[i] == "Success":
                        if output[i].strip() == correct_output[i][0]:
                            response["TestCases"]["Errormessage"][i] = None
                            response["TestCases"]["Status"][i] = "Passed"
                            score += correct_output[i][1]
                        else:
                            response["TestCases"]["Errormessage"][i] = None
                            response["TestCases"]["Status"][i] = "Wrong Answer"

                if response["Submission Status"] is None:
                    if len(message) == message.count("Passed"):
                        response["Submission Status"] = "AC"
                    else:
                        response["Submission Status"] = "WA"

            response["Score"] = score
            if time is not None:
                response["Time"] = sum(time)
            if memory is not None:
                response["Memory"] = sum(memory)
            response['status_check']=True
            print response
            return JSONResponse(response)

        except Exception as e:
            traceback_string = traceback.format_exc()
            response = {
                'message': 'Failed to Submit',
                'status_check': False,
                'Submission_status': 'Judge has Some Issue',
                'exception': e.message,
                'traceback_string' : traceback_string
            }

            return JSONResponse(response)
