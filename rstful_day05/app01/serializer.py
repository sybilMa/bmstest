
from rest_framework.serializers import ModelSerializer
from app01 import models
class PublishSerializers(ModelSerializer):
    class Meta:
        model=models.Publish
        fields="__all__"