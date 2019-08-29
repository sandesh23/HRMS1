from django.db import models

# Create your models here.


class BasicInfo(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email_id = models.EmailField(null=False, unique=True)
    nic = models.CharField(max_length=16, unique=True, null=False)
    image = models.ImageField(upload_to='documents/')
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
    role_name = models.CharField(max_length=50, null=False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.DateTimeField(auto_now_add=True, blank=True)
    is_deleted = models.BooleanField(default=True, null=False)

    class Meta:
        db_table = 'Role'


class Degree(models.Model):
    degree_id = models.IntegerField(primary_key=True)
    degree_name = models.CharField(max_length=50, null=False)
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
    location_id = models.CharField(primary_key=True, max_length=50)
    location_name = models.CharField(max_length=50, null=False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, null=False)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.TimeField(auto_now_add=True, null=False)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = 'Location'


class SourceOfHire(models.Model):
    source_id = models.CharField(primary_key=True, max_length=50)
    source_name = models.CharField(max_length=50, null=False)
    added_by = models.CharField(max_length=50, null=False)
    added_time = models.DateTimeField(auto_now_add=True, blank=True)
    modified_by = models.CharField(max_length=50, null=False)
    modified_time = models.TimeField(auto_now_add=True, null=False)
    is_deleted = models.BooleanField(default=True)

    class Meta:
        db_table = 'SourceOfHire'


class EmployeeType(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=50)
    emp_type = models.CharField(max_length=50, null=False)
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


class PersonalDetails(models.Model):
    ID = models.IntegerField(primary_key=True)
    Employee_id = models.IntegerField(max_length=50, null=False)
    mobile = models.IntegerField(max_length=10, null=False)
    gender = models.CharField(max_length=3, null=False)
    blood_group = models.CharField(max_length=10, null=False)
    other_mobile = models.IntegerField(max_length=10)
    date_of_birth = models.DateField(null=True)
    permanent_address = models.CharField(max_length=50, null=False)
    present_address = models.CharField(max_length=10, null=False)
    maretial_status = models.CharField(max_length=1, null=False)
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
    emp_id = models.IntegerField(max_length=50, null=False)
    previous_company = models.CharField(max_length=50, null=False)
    job_id = models.IntegerField(max_length=50, null=False)
    from_date = models.DateTimeField(null=False)
    to_date = models.DateTimeField(null=False)

    class Meta:
        db_table = 'work_experience'


class Education(models.Model):
    education_id = models.IntegerField(primary_key=True)
    emp_id = models.ForeignKey(BasicInfo,null=False)
    degree_id = models.ForeignKey(Degree,null=False)
    field = models.ForeignKey(Degree, on_delete=models.CASCADE)
    date_of_completion = models.DateField(null=False)
    additional_notes = models.CharField(max_length=50)

    class Meta:
        db_table = 'education'


class WorkDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_id = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation_id = models.ForeignKey(Designation, on_delete=models.CASCADE)
    reporting_to = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    Date_of_Joining = models.DateField(null=False)
    PAN_number = models.CharField(max_length=10, unique=True, null=False)
    apprisal_manager = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    seating_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    mentor = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    source_id = models.ForeignKey(SourceOfHire, on_delete=models.CASCADE)
    employee_type = models.ForeignKey(EmployeeType, on_delete=models.CASCADE)
    employee_Status = models.BooleanField(null=False)

    class Meta:
        db_table = 'work_details'


class Summary(models.Model):
    id = models.IntegerField(primary_key=True)
    emp_Id = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    job_description = models.CharField(max_length=300)
    about_me = models.CharField(max_length=300)
    expertise = models.CharField(max_length=300)

    class Meta:
        db_table = 'summary'


class Dependant(models.Model):
    dependant_id = models.IntegerField(primary_key=True)
    emp_Id = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    relationship = models.CharField(max_length=50, null=False)
    dob = models.DateField(blank=True)

    class Meta:
        db_table = 'dependant'
