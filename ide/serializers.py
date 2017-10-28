from rest_framework import serializers

from ide import Languages


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Languages
        fields = ('display_name', 'language_code', 'version')