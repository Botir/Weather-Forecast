import datetime
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from .search import get_forecast

class ForecastView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):

        if 'date' in request.query_params and request.query_params['date']:
            dt = request.query_params['date']
            self.validate_date(dt)
        else:
            raise ParseError('Missing date format parameter')


        if 'country_code' in request.query_params and request.query_params['country_code']:
            country_code = request.query_params['country_code']
        else:
            raise ParseError('Missing parameter country_code')
        result = get_forecast(dt, country_code)
        return Response({'forecast': result}, status=status.HTTP_200_OK, content_type='application/json')

    def validate_date(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ParseError("Incorrect data format, should be YYYY-MM-DD")