# _*_ encoding:utf-8 _*_
import logging
import datetime

import json_log_formatter
from django.conf import settings

__author__ = 'nzb'
__datetime__ = '2020/11/19 9:55'
__doc__ = ''


class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):
    def json_record(self, message: str, extra: dict, record: logging.LogRecord):
        django = {
            'app': settings.APP_ID,  # 应用id
            'name': record.name,  # loggers 名
            'pathname': record.pathname, # 文件路径
            'filename': record.filename,  # 文件名
            'fileno': record.lineno,  # 记录所在行
            'exc_text': record.exc_text,  # 日志信息
            'funcName': record.funcName,  # 函数名
            'msecs': record.msecs,
        }
        if record.exc_info:
            django['exc_info'] = self.formatException(record.exc_info)

        return {
            'message': message,  # 记录的信息
            'create_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'level': record.levelname,
            'context': extra,  # extra 额外信息
            'django': django
        }
