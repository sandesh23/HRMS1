from django.db import models

# Create your models here.


class BasicInfo(models.Model):
    ''' nic = national identification code '''
    emp_id = models.CharField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email_id = models.EmailField(null=False, unique=True)
    nic = models.CharField(max_length=16, unique=True,null=False)
    image = models.ImageField(upload_to='documents/%Y%M%d/',max_length=100)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 'Basic_info'

class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=50, null=False, unique=True)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 'Department'

class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=50, null= False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 'Role'


class Degree(models.Model):
    degree_id = models.IntegerField(primary_key=True)
    degree_name = models.CharField(max_length=50, null= False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 'Degree'

class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'State'

class Designation(models.Model):
    designation_id = models.IntegerField(primary_key=True)
    designation_name = models.CharField(max_length=50, null=False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 'Designation'

class Location(models.Model):
    location_id = models.CharField(primary_key=True,max_length=50)
    location_name =models.CharField(max_length=50,null=False)
    added_by=models.CharField(max_length=50,null=False)
    added_time=models.DateTimeField(auto_now_add=True,null=False)
    modified_by=models.CharField(max_length=50,null=False)
    modified_time=models.TimeField(auto_now_add=True,null=False)
    is_deleted=models.BooleanField(default=True)

    class Meta:
        db_table = 'Location'

class SourceOfHire(models.Model):
    source_id=models.CharField(primary_key=True,max_length=50)
    source_name=models.CharField(max_length=50,null=False)
    added_by=models.CharField(max_length=50,null=False)
    added_time=models.DateTimeField(auto_now_add=True,blank=True)
    modified_by=models.CharField(max_length=50,null=False)
    modified_time=models.TimeField(auto_now_add=True,null=False)
    is_deleted=models.BooleanField(default=True)

    class Meta:
        db_table ='SourceOfHire'

class EmployeeType(models.Model):
    emp_id =models.CharField(primary_key=True,max_length=50)
    emp_type =models.CharField(max_length=50,null=False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.TimeField(auto_now_add=True, null=False)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = 'EmployeeType'

class JobTitle(models.Model):
    job_id = models.CharField(primary_key=True, max_length=50)
    job_title = models.CharField(max_length=50, null=False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.TimeField(auto_now_add=True, null=False)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = 'JobTitle'

class Country(models.Model):
    country_id = models.CharField(primary_key=True, max_length=50)
    country_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'Country'
