from . import models
from rest_framework import serializers
from .models import *


class PrioritySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Priority
        fields = ('__all__')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ('__all__')


class JobTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobType
        fields = ('__all__')


class RequestTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RequestType
        fields = ('__all__')


class CaseStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaseStatus
        fields = ('__all__')


class ReligionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Religion
        fields = ('__all__')


class NationalitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nationality
        fields = ('__all__')


class JobPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobPosition
        fields = ('__all__')


class JobGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobGroup
        fields = ('url', 'name', 'min_salary', 'max_salary', 'active')
#
#
# class ProbationTypesSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         models = ProbationTypes
#         fields = ('url','name','active')


class EmploymentTermsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmploymentTerms
        fields = ('__all__')