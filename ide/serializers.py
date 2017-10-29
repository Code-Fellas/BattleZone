from rest_framework import serializers

from ide.models import Languages


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Languages
        fields = ('display_name', 'language_code', 'hackerrank_name')