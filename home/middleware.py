from django.utils.deprecation import MiddlewareMixin

from django.utils.deprecation import MiddlewareMixin

class CustomFrameOptionsMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        host = request.META.get('HTTP_HOST', '')
        # Allow framing for both your local test tunnel and your live domain
        if 'starliftandcontroller.xyz' in host or 'ngrok' in host:
            response['X-Frame-Options'] = 'ALLOWALL'
        return response