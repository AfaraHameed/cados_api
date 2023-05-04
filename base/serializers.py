from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Advocates,Company

class CompanySerializer(ModelSerializer):
    employee_count= SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self,obj):
        count=obj.advocates_set.count()
        return count

class AdvocateSerializer(ModelSerializer):
    company=CompanySerializer()
    class Meta:
        model = Advocates
        fields=['username','bio','company']



