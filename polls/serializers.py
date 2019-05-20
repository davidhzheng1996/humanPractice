from rest_framework import serializers
from .models import *

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = '__all__'

# class WordSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Word
#         fields = '__all__'

# class WordToAnalysisSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Word_To_Analysis
#         fields = '__all__'