from rest_framework import serializers

from contest.models import Contests, Problem


class ContestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contests
        fields = ('title', 'contest_code', 'date', 'start_time', 'end_time', 'duration')


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = ('title', 'problem_code', 'problem_statement')