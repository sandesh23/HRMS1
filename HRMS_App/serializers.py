from .models import *
from rest_framework.serializers import ModelSerializer


class BasicInfoSerializer(ModelSerializer):
    class Meta:
        model = BasicInfo
        fields = "__all__"


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class DegreeSerializer(ModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"


class StateSerializer(ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class DesignationSerializer(ModelSerializer):
    class Meta:
        model = Designation
        fields = "__all__"


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class SourceOfHireSerializer(ModelSerializer):
    class Meta:
        model = SourceOfHire
        fields = "__all__"


class EmployeeTypeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeType
        fields = "__all__"


class JobTitleSerializer(ModelSerializer):
    class Meta:
        model = JobTitle
        fields = "__all__"


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
