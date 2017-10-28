from rest_framework.views import APIView

from ide.models import Languages
from ide.serializers import LanguageSerializer
from middleware.response import JSONResponse


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
        cod
