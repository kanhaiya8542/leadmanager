from rest_framework import serializers
from leadmanager.leads.models import Lead


# Lead Serializer
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields ='_all_'