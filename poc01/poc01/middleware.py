import os
import psutil
import sys
from django.utils.deprecation import MiddlewareMixin

THRESHOLD = 0

class MemoryUsageMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request._mem = psutil.Process(os.getpid()).memory_info()

    def process_response(self, request, response):
        mem = psutil.Process(os.getpid()).memory_info()
        diff = mem.rss - request._mem.rss
        if diff > THRESHOLD:
            diff_in_mb = diff / (1024 * 1024) 
            print("Memory usage increased by {} MB".format(diff_in_mb))
        return response
