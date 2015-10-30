import logging
import socket
import time

from django.conf import settings

class RequestLogMiddleware(object):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):

        log_data = {
            'user': request.user.pk,

            'remote_address': request.META['REMOTE_ADDR'],
            'server_hostname': socket.gethostname(),

            'request_method': request.method,
            'request_path': request.get_full_path(),
            'response_status': response.status_code,

            'run_time': time.time() - request.start_time,
        }

        if settings.DEBUG:
            print log_data

        logger = logging.getLogger()
        logger.info(str(log_data))

        return response
