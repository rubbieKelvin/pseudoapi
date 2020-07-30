from .models import PseudoApi
from rest_framework.serializers import ModelSerializer

class PseudoApiSerialzer(ModelSerializer):
	class Meta:
		model = PseudoApi
		fields = "__all__"
		read_only_fields = ["id", "date_created", "route"]