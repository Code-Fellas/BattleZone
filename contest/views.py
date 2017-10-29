from django.shortcuts import render
import traceback
from rest_framework.views import APIView
from contest.models import Contests, Problem, Testcases
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


class CreateContestView(APIView):

    def post(self, request):
        try:
            print request.data
            unique_code = request.data['contest_code']
            contest_name = request.data['contest_name']
            contest_date = request.data['contest_date']
            problems = request.data['prob_data']
            total_problems = request.data['total_problems']
            contest_start_time = request.data['contest_start_time']
            contest_end_time = request.data['contest_end_time']
            contest_duration = request.data['duration']

            new_contest = Contests.objects.create(
                                        title=contest_name,
                                        date=contest_date,
                                        contest_code=unique_code,
                                        start_time=contest_start_time,
                                        end_time=contest_end_time,
                                        duration=contest_duration
                                        )

            for i in range(total_problems):
                print problems[i]
                problem_name = problems[i]['problem_name']
                problem_code = problems[i]['problem_code']
                problem_statement = problems[i]['problem_statement']
                total_samples = problems[i]['total_st']
                total_test_cases = problems[i]['total_tc']
                sample_test_cases_inputs = problems[i]['sample_test_cases_inputs']
                sample_test_cases_outputs = problems[i]['sample_test_cases_outputs']
                test_cases_inputs = problems[i]['test_cases_inputs']
                test_cases_outputs = problems[i]['test_cases_outputs']

                new_problem = Problem.objects.create(
                                            title=problem_name,
                                            problem_code=problem_code,
                                            problem_statement=problem_statement,
                                            contest=new_contest
                                        )

                for j in range(total_samples):
                    new_sample = Testcases.objects.create(
                                            problem=new_problem,
                                            input=sample_test_cases_inputs[j],
                                            output=sample_test_cases_outputs[j],
                                            is_sample=True,
                                            marks=20
                                        )
                    print str(new_sample.id)+' created'

                for j in range(total_test_cases):
                    new_tc = Testcases.objects.create(
                                            problem=new_problem,
                                            input=test_cases_inputs[j],
                                            output=test_cases_outputs[j],
                                            is_sample=False,
                                            marks=20
                                        )
                    print str(new_tc.id) + ' created'

            response = {
                'status': True,
                'message': 'Created contest' + contest_name + '@ ' + unique_code,
                #'status': 'contest id is ' + str(new_contest.id)
            }
            return JSONResponse(response)

        except Exception as e:
            traceback_string = traceback.format_exc()
            print traceback_string

            response = {
                'message': 'Failed to Create New User',
                'status': False,
                'exception': e.message
            }

            return JSONResponse(response)
