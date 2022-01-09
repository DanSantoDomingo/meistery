


from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie_extras.resource import MultipartResourceMixin
from core.models import Request


class RequestResource(MultipartResourceMixin, ModelResource ):
    class Meta:
        queryset = Request.objects.all()
        resource_name = 'requests'
        authorization = Authorization()


request_resource = RequestResource()