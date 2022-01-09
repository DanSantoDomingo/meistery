


from tastypie.api import Api
from .resources import request_resource


v1_api = Api(api_name='v1')
v1_api.register(request_resource)