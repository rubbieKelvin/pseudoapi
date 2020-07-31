from .models import PseudoApi
from .serializers import PseudoApiSerialzer

from urllib.parse import unquote
from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_405_METHOD_NOT_ALLOWED, HTTP_200_OK, HTTP_206_PARTIAL_CONTENT, HTTP_400_BAD_REQUEST

# Create your views here.
class PsuedoApiListCreateView(views.APIView):
	def get(self, request):
		queryset = PseudoApi.objects.all()
		serializer = PseudoApiSerialzer(queryset, many=True)
		return Response(serializer.data)

	@csrf_exempt
	def post(self, request):
		method = request.data.get("method")
		request_body_template = request.data.get("body_request")
		response_body_template = request.data.get("body_response")

		if request_body_template is None: return Response(dict(error="body_request"), status=HTTP_206_PARTIAL_CONTENT)
		if response_body_template is None: return Response(dict(error="body_response"), status=HTTP_206_PARTIAL_CONTENT)
		if method is None: return Response(dict(error="method"), status=HTTP_206_PARTIAL_CONTENT)

		newapi = PseudoApi(
			method=method,
			body_request=request_body_template,
			body_response=response_body_template
		)

		newapi.save()		# genrate id
		newapi.makeroute()	# genarate route
		newapi.save()		# save

		serializer = PseudoApiSerialzer(newapi)
		
		return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET", "POST"])
def call_pseudoapi(request, route):
	route = unquote(route)
	apimodel:PseudoApi = PseudoApi.objects.filter(route=route).first()

	if apimodel:
		if apimodel.method.lower() == request.method.lower():
			response = apimodel.generateresponse(request.data, [])

			if response:
				return Response(response, HTTP_200_OK)

			else:
				return Response(dict(error="error in request body", template=apimodel.body_request), status=HTTP_400_BAD_REQUEST)

		else:
			return Response(dict(
				error="method not allowed"
			), status=HTTP_405_METHOD_NOT_ALLOWED)

	else:
		return Response(dict(
			error="api does not exist"
		), status=HTTP_404_NOT_FOUND)