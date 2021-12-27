from rest_framework import serializers
from events.models import client,project

class clientserializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields =('id','client_name','created_at','created_by')

class projectserializer(serializers.ModelSerializer):
    class Meta:
        model = project 
        fields ='__all__'