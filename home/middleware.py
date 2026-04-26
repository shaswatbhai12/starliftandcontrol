from django.utils.deprecation import MiddlewareMixin

# Change 'CustomFrameOptionsMiddleware' to 'AllowNgrokInFrameMiddleware'
class AllowNgrokInFrameMiddleware(MiddlewareMixin): 
    def process_response(self, request, response):
        host = request.META.get('HTTP_HOST', '')
        if 'starliftandcontroller.xyz' in host or 'ngrok' in host:
            response['X-Frame-Options'] = 'ALLOWALL'
        return response