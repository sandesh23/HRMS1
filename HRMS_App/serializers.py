from .models import *
from rest_framework.serializers import ModelSerializer


class BasicInfoSerializer(ModelSerializer):
    class Meta:
        model = BasicInfo
        fields = ['emp_id','first_name','middle_name','last_name','email_id','nic','image']


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ['dept_id','dept_name']


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['role_id','role_name']


class DegreeSerializer(ModelSerializer):
    class Meta:
        model = Degree
        fields = ['degree_id','degree_name']


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class DesignationSerializer(ModelSerializer):
    class Meta:
        model = Designation
        fields = ['designation_id','designation_name']


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_id','location_name']


class SourceOfHireSerializer(ModelSerializer):
    class Meta:
        model = SourceOfHire
        fields = ['source_id','source_name']


class EmployeeTypeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeType
        fields = ['emp_id','emp_type']


class JobTitleSerializer(ModelSerializer):
    class Meta:
        model = JobTitle
        fields = ['job_id','job_title']


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class PersonalDetailsSerializer(ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = "__all__"


class WorkExperienceSerializer(ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = "__all__"


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class WorkDetailsSerializer(ModelSerializer):
    class Meta:
        model = WorkDetails
        fields = "__all__"


class SummarySerializer(ModelSerializer):
    class Meta:
        model = Summary
        fields = "__all__"


class DependantSerializer(ModelSerializer):
    class Meta:
        model = Dependant
        fields = "__all__"
