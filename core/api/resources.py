


from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.validation import FormValidation
from tastypie_extras.resource import MultipartResourceMixin


from core.models import Request
from core.forms import RequestForm



class RequestResource(MultipartResourceMixin, ModelResource ):
    class Meta:
        queryset = Request.objects.all()
        resource_name = 'requests'
        authorization = Authorization()
        validation = FormValidation(form_class=RequestForm)

request_resource = RequestResource()