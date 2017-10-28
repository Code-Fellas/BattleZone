from rest_framework import serializers

from contest.models import Contests


class ContestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contests
        fields = ('title', 'contest_code', 'date', 'start_time', 'end_time', 'duration')