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
    image = models.ImageField(upload_to='documents/')
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)


class Department(models.Model):
    dept_id = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=50, null=False, unique=True)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)


class Role(models.Model):
    role_id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=50, null= False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)


class Degree(models.Model):
    degree_id = models.IntegerField(primary_key=True)
    degree_name = models.CharField(max_length=50, null= False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)


class state(models.model):
    state_id = models.IntegerField(primary_key=True)
    state_name = models.CharField(max_length=50, null=False)


class Designation(models.model):
    designation_id = models.IntegerField(primary_key=True)
    designation_name = models.CharField(max_length=50, null=False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)


