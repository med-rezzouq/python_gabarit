from rest_framework import serializers
from .models import *
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Choice
        fields='__all__'# sinon ['champs1','champs2',...]
        extra_kwargs = {"votes":{"min_value":1,"max_value":1000, }}

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields='__all__'# sinon ['champs1','champs2',...]


