from .models import *
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from HRMS_Project.Logger import *

class UserSerializer(ModelSerializer):
    logger.info("Inside User Serializer")

    class Meta:
        model = User
        fields = '__all__'

    logger.info("User Serializer Executed")

class BasicInfoSerializer(ModelSerializer):
    logger.info("Inside Basic Info Serializer")
    class Meta:
        model = BasicInfo
        fields = ['emp_id','first_name','middle_name','last_name','email_id','nic','image']

    logger.info("Basic Info Serializer Executed")


class DepartmentSerializer(ModelSerializer):
    logger.info("Inside Department Serializer")

    class Meta:
        model = Department
        fields = ['dept_id','dept_name']

    logger.info("Department Serializer Executed")


class RoleSerializer(ModelSerializer):
    logger.info("Inside Role Serializer")
    class Meta:
        model = Role
        fields = ['role_id','role_name']

    logger.info("Role Serializer Executed")


class DegreeSerializer(ModelSerializer):
    logger.info("Inside Role Serializer")

    class Meta:
        model = Degree
        fields = ['degree_id','degree_name']
    logger.info(" Role Serializer Executed")


class StateSerializer(ModelSerializer):
    logger.info("Inside State Serializer")

    class Meta:
        model = State
        fields = "__all__"

    logger.info("State Serializer Executed")


class DesignationSerializer(ModelSerializer):
    logger.info("Inside Designation Serializer")
    class Meta:
        model = Designation
        fields = ['designation_id','designation_name']

    logger.info("Designation Serializer Executed ")


class LocationSerializer(ModelSerializer):
    logger.info("Inside Location Serializer")

    class Meta:
        model = Location
        fields = ['location_id','location_name']
    logger.info("Location Serializer Executed")


class SourceOfHireSerializer(ModelSerializer):
    logger.info("Inside Source of Hire Serializer")

    class Meta:
        model = SourceOfHire
        fields = ['source_id','source_name']
    logger.info("Source of Hire Serializer executed")


class EmployeeTypeSerializer(ModelSerializer):
    logger.info("Inside Employee Serializer")

    class Meta:
        model = EmployeeType
        fields = ['emp_id','emp_type']

    logger.info("Employee Serializer Executed")


class JobTitleSerializer(ModelSerializer):
    logger.info("Inside JobTitle Serializer ")

    class Meta:
        model = JobTitle
        fields = ['job_id','job_title']
    logger.info("Job Title Serializer executed")


class CountrySerializer(ModelSerializer):
    logger.info("Inside Country Serializer ")
    class Meta:
        model = Country
        fields = "__all__"

    logger.info("Country Serializer Executed ")


class PersonalDetailsSerializer(ModelSerializer):
    logger.info("Inside Personal Detail Serializer ")

    class Meta:
        model = PersonalDetails
        fields = "__all__"

    logger.info("Personal Detail Serializer Executed ")


class WorkExperienceSerializer(ModelSerializer):
    logger.info("Inside Work Experience Serializer")
    class Meta:
        model = WorkExperience
        fields = "__all__"
    logger.info("Work Experience Serializer Executed")


class EducationSerializer(ModelSerializer):
    logger.info("Inside Education Serializer")

    class Meta:
        model = Education
        fields = "__all__"

    logger.info("Education Serializer Executed")


class WorkDetailsSerializer(ModelSerializer):
    logger.info("Inside Work Detail Serializer ")

    class Meta:
        model = WorkDetails
        fields = "__all__"

    logger.info("Workdetail Serializer Executed ")


class SummarySerializer(ModelSerializer):
    logger.info("Inside Summery Serializer")
    class Meta:
        model = Summary
        fields = "__all__"
    logger.info("Summary serializer Executed")


class DependantSerializer(ModelSerializer):
    logger.info("Inside Dependent Serializer ")

    class Meta:
        model = Dependant
        fields = "__all__"

    logger.info("Depenednts Serializer Executed")