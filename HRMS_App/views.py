from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout,login,authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

class EmpInfoViewSet(ModelViewSet):
    queryset = EmpInfo.objects.all()
    serializer_class = EmpInfoSerializer


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






@csrf_exempt
def add_user(request):

    User.objects.create_user(first_name=request.POST['first_name'],last_name=request.POST['last_name'],
                   email=request.POST['email'],username=request.POST['username'],
                   password=request.POST['password'],is_superuser=request.POST['is_superuser'],
                   is_staff =request.POST['is_staff'])
    return HttpResponse('new user added successfully')


@csrf_exempt
def log_in(request):
    username = request.POST['username']
    password = request.POST['password']
    if username and password:
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return HttpResponse("user log in successful")
        else:
            raise ValidationError("not valid user")
    else:
        return ValidationError("provide data")




@login_required
def log_out(request):
    print('inside log out')
    logout(request)
    return HttpResponse("log out successful")

