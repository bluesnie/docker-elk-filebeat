import logging

from rest_framework.response import Response
from rest_framework.views import APIView


class Debug(APIView):

    def get(self, request):
        logging.getLogger("print").debug("This is debug message", extra={'extraParam': 'Gonzalo'})

        return Response(data={'debug', 'hello'})


class Error(APIView):

    def get(self, request):
        logging.getLogger("print").error("This is error message")

        return Response(data={'error', 'hello'})


class Info(APIView):

    def get(self, request):
        logging.getLogger("print").info("This is info message")

        return Response(data={'info', 'hello'})
