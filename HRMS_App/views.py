from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class BasicInfoViewSet(ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicInfoSerializer


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class DegreeViewSet(ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer


class StateViewSet(ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class DesignationViewSet(ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class SourceOfHireViewSet(ModelViewSet):
    queryset = SourceOfHire.objects.all()
    serializer_class = SourceOfHireSerializer


class EmployeeTypeViewSet(ModelViewSet):
    queryset = EmployeeType.objects.all()
    serializer_class = EmployeeTypeSerializer


class JobTitleViewSet(ModelViewSet):
    queryset = JobTitle.objects.all()
    serializer_class = JobTitleSerializer


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class PersonalDetailsViewSet(ModelViewSet):
    queryset = PersonalDetails.objects.all()
    serializer_class = PersonalDetailsSerializer


class WorkExperienceViewSet(ModelViewSet):
    queryset = WorkExperience.objects.all()
    serializer_class = WorkExperienceSerializer


class EducationViewSet(ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class WorkDetailViewSet(ModelViewSet):
    queryset = WorkDetails.objects.all()
    serializer_class = WorkDetailsSerializer


class SummaryViewSet(ModelViewSet):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer


class DependantViewSet(ModelViewSet):
    queryset = Dependant.objects.all()
    serializer_class = DependantSerializer





