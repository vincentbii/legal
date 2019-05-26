# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route

from rest_framework import viewsets
from .serializers import (
    PrioritySerializer, DepartmentSerializer, JobTypeSerializer, RequestTypeSerializer, CaseStatusSerializer, ReligionSerializer, NationalitySerializer, EmploymentTermsSerializer, JobPositionSerializer
)
from .models import (
    Priority, Department, JobType, RequestType, CaseStatus, Religion, Nationality, EmploymentTerms, JobPosition
)


# Create your views here.
class PriorityViewSet(viewsets.ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class JobTypeViewSet(viewsets.ModelViewSet):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer

    @list_route(methods=['POST'])
    def deleteall(self, request, pk=None):
        queryset = JobType.objects.all()
        serializer_class = JobTypeSerializer(queryset, many=True)
        l = request.data
        for i in l:
            # a.append(i)
            dele = JobType.objects.get(id=i)
            dele.delete()
        return Response(serializer_class.data)


class RequestTypeViewSet(viewsets.ModelViewSet):
    queryset = RequestType.objects.all()
    serializer_class = RequestTypeSerializer


# class JobGroupViewSet(viewsets.ModelViewSet):
#     queryset = JobGroup
#     serializer_class = JobGroupSerializer


# class RequestTypeViewSet(viewsets.ModelViewSet):
#     queryset = RequestType
#     serializer_class = RequestTypeSerializer


class CaseStatusViewSet(viewsets.ModelViewSet):
    queryset = CaseStatus.objects.all()
    serializer_class = CaseStatusSerializer


class ReligionViewSet(viewsets.ModelViewSet):
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer


class JobPositionViewSet(viewsets.ModelViewSet):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer


# class ProbationTypeViewSet(viewsets.ModelViewSet):
#     queryset = ProbationTypes
#     serializer_class = ProbationTypesSerializer


class EmploymentTermsViewSet(viewsets.ModelViewSet):
    queryset = EmploymentTerms.objects.all()
    serializer_class = EmploymentTermsSerializer


class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer
