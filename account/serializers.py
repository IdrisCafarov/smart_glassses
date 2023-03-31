from rest_framework import serializers
from .models import *


class CreateCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallHelp
        fields = ['user','place','condition']