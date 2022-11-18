from rest_framework import serializers
from .models import book
class Book_Serializers(serializers.ModelSerializer):
    class Meta:
        model=book
        fields=['tittle','content','created_at','image','caticory']
