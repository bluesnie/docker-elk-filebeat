import logging
import traceback
import socket
import json

from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response


class LogsMiddleware(MiddlewareMixin):
    """
    日志中间件
    """

    def process_response(self, request, response):
        """process_request 和 process_view 中的 request 都不能获取用户信息，还没有再次封装 request"""
        info = self.get_extra_info(request, response=response)
        logger = logging.getLogger("request_response")
        logger.info("中间件 process_response", extra={"write_loc": "middleware_response", "info": info})
        return response

    def process_exception(self, request, exception):
        """异常处理"""
        info = self.get_extra_info(request, exception=exception)
        logger = logging.getLogger("exception")
        logger.error(exception, extra={"write_loc": "middleware_exception", "info": info})

    @staticmethod
    def get_extra_info(request, response=None, exception=None):
        """获取请求、返回或异常信息"""

        request_data = LogsMiddleware.get_request_info(request)
        response_data = LogsMiddleware.get_response_info(response)
        exception_data = traceback.format_exc() if exception is not None else ""
        user_data = LogsMiddleware.get_user_info(request)

        return {
            "user": user_data,
            "request": request_data,
            "response": response_data,
            "exception": exception_data
        }

    @staticmethod
    def get_user_info(request):
        return {
            "id": request.user.id,
            "username": request.user.phone if request.user.id else request.user.username
        }

    @staticmethod
    def get_request_info(request):

        try:
            body = json.loads(request.body)
        except Exception:
            body = dict()

        if request.method == "GET":
            body.update(dict(request.GET))
        else:
            body.update(dict(request.POST))

        request_data = {
            "method": request.method,
            "path": request.path,
            "path_info": request.path_info,
            "body": body,
            "sip": request.META.get('REMOTE_ADDR', ''),
            "dip": socket.gethostbyname(socket.gethostname()),
        }

        return request_data

    @staticmethod
    def get_response_info(response):
        if response is not None:

            if isinstance(response, Response):
                data = response.data
            else:
                data = {}
            response_data = {
                "status_code": response.status_code,
                "reason_phrase": response.reason_phrase,
                "data": data
            }
        else:
            response_data = {
                "status_code": None,
                "reason_phrase": None,
                "data": None
            }

        return response_data
