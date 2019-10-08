from django.db import models
from .validators import *
from django.core.validators import validate_image_file_extension
# Create your models here.

class CommonAbstract(models.Model):
    added_by = models.CharField(max_length=50, null=False,validators=[name_validators])
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=False)

    class Meta:
        abstract = True


class EmpInfo(CommonAbstract):
    emp_id = models.CharField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=50, null=False,validators=[name_validators])
    middle_name = models.CharField(max_length=50, null=False,validators=[name_validators])
    last_name = models.CharField(max_length=50, null=False,validators=[name_validators])
    email_id = models.EmailField(null=False, unique=True,validators=[email_validator])
    nic = models.CharField(max_length=16, null=False,validators=[name_validators])
    image = models.ImageField(upload_to='documents/%Y/%m/%d/', max_length=100,validators=[validate_image_file_extension])


    class Meta:
        db_table = 'Emp_info'


class Department(CommonAbstract):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=50, null=False, unique=True,validators=[name_validators])


    class Meta:
        db_table = 'Department'



class Role(CommonAbstract):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=50, null=False,validators=[name_validators])
    mobile = models.CharField(max_length=13, null=False, validators=[mobile_regex])


    class Meta:
        db_table = 'Role'


class Degree(CommonAbstract):
    degree_id = models.IntegerField(primary_key=True)
    degree_name = models.CharField(max_length=50, null=False,validators=[name_validators])

    class Meta:
        db_table = 'Degree'


class Country(models.Model):
    country_id = models.CharField(primary_key=True, max_length=50)
    country_name = models.CharField(max_length=50, null=False,validators=[name_validators])

    class Meta:
        db_table = 'Country'

#c1=Country(country_id=111,country_name='Pune')
class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    state_name = models.CharField(max_length=50, null=False,validators=[name_validators])

    class Meta:
        db_table = 'State'

#State(state_id=2233,state_name='MH',country=111)
class Designation(CommonAbstract):
    designation_id = models.IntegerField(primary_key=True)
    designation_name = models.CharField(max_length=50, null=False)


    class Meta:
        db_table = 'Designation'


class Location(CommonAbstract):
    location_id = models.CharField(primary_key=True, max_length=50)
    location_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'Location'


class SourceOfHire(CommonAbstract):
    source_id = models.CharField(primary_key=True, max_length=50)
    source_name = models.CharField(max_length=50, null=False)


    class Meta:
        db_table = 'SourceOfHire'


class EmployeeType(CommonAbstract):
    emp_id = models.CharField(primary_key=True, max_length=50)
    emp_type = models.CharField(max_length=50, null=False)


    class Meta:
        db_table = 'EmployeeType'


class JobTitle(CommonAbstract):
    job_id = models.CharField(primary_key=True, max_length=50)
    job_title = models.CharField(max_length=50, null=False)


    class Meta:
        db_table = 'JobTitle'


class PersonalDetails(models.Model):
    ID = models.IntegerField(primary_key=True)
    Employee_id = models.IntegerField(null=False)
    mobile = models.CharField(max_length=13, null=False, validators=[mobile_regex])
    gender = models.CharField(max_length=3,choices=[('M','Male'),('F','Female')])
    blood_group = models.CharField(max_length=10, null=False)
    other_mobile = models.CharField(max_length=13,validators=[mobile_regex])
    date_of_birth = models.DateField(null=True)
    permanent_address = models.CharField(max_length=50, null=False)
    present_address = models.CharField(max_length=10, null=False)
    marital_status = models.CharField(max_length=3,choices=[('M','Married'),('U','Unmarried')])
    age = models.FloatField(null=False)
    wedding_date = models.DateField()
    spouse_name = models.CharField(max_length=50)
    about_me = models.CharField(max_length=500)
    relieving_date = models.DateField(null=False)
    tags = models.CharField(max_length=10)

    class Meta:
        db_table = 'personal_details'


class WorkExperience(models.Model):
    id = models.IntegerField(primary_key=True)
    emp_id = models.IntegerField(null=False)
    previous_company = models.CharField(max_length=50, null=False)
    job_id = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    from_date = models.DateTimeField(null=False)
    to_date = models.DateTimeField(null=False)

    class Meta:
        db_table = 'work_experience'


class Education(models.Model):
    education_id = models.IntegerField(primary_key=True)
    emp_id = models.ForeignKey(EmpInfo, null=False, on_delete=models.CASCADE)
    degree_id = models.ForeignKey(Degree, null=False,on_delete=models.CASCADE)
    field = models.CharField(max_length=100, null=False)
    date_of_completion = models.DateField(null=False)
    additional_notes = models.CharField(max_length=50)

    class Meta:
        db_table = 'education'


class WorkDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_id = models.ForeignKey(EmpInfo, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE)
    reporting_to = models.ForeignKey(EmpInfo, on_delete=models.CASCADE, related_name='basic_info_reported_by')
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    Date_of_Joining = models.DateField(null=False)
    PAN_number = models.CharField(max_length=10, unique=True, null=False)
    appraisal_manager = models.ForeignKey(EmpInfo, on_delete=models.CASCADE, related_name='appraisal_manager')
    seating_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location')
    mentor = models.ForeignKey(EmpInfo, on_delete=models.CASCADE, related_name='mentor')
    source_id = models.ForeignKey(SourceOfHire, on_delete=models.CASCADE)
    employee_type = models.ForeignKey(EmployeeType, on_delete=models.CASCADE)
    employee_Status = models.BooleanField(null=False)

    class Meta:
        db_table = 'work_details'


class Summary(models.Model):
    id = models.IntegerField(primary_key=True)
    emp_Id = models.ForeignKey(EmpInfo, on_delete=models.CASCADE)
    job_description = models.CharField(max_length=300)
    about_me = models.CharField(max_length=300)
    expertise = models.CharField(max_length=300)

    class Meta:
        db_table = 'summary'


class Dependant(models.Model):
    dependant_id = models.IntegerField(primary_key=True)
    emp_Id = models.ForeignKey(EmpInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    relationship = models.CharField(max_length=50, null=False)
    dob = models.DateField(blank=True)

    class Meta:
        db_table = 'dependant'
