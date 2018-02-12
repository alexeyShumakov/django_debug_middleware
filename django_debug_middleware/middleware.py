import logging, time

logger = logging.getLogger(__name__)


class DebugMiddleware:
    def __init__(self):
        self.start = None

    def process_request(self, _request):
        self.start = time.time()

    def process_response(self, request, response):
        delta = (time.time() - self.start) * 1000.0
        info = '%s %s in %s ms' % (request.method, request.path, delta)
        logger.debug(info)
        return response 
