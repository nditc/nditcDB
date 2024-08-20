from django.db import models
# import uuid

BLOOD_GRP_CHOICES = (
    ('a+','A+'),
    ('a-','A-'),
    ('b+','B+'),
    ('b-','B-'),
    ('o+','O+'),
    ('o-','O-'),
    ('ab+','AB+'),
    ('ab-','AB-'),
)
YEAR = (
    (2025,'2023-24'),
    (2024,'2022-23'),
    (2023,'2021-22'),
    (2022,'2020-21'),
    (2021,'2019-20'),
    (2020,'2018-19'),
    (2019,'2017-18'),
)

class Member(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    year = models.IntegerField(choices=YEAR)
    name = models.CharField(max_length=20)
    admission_serial = models.CharField(max_length=20,null=True,blank=True)
    college_roll = models.CharField(null=True,max_length=10,blank=True)
    serial = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=15,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    transection_id = models.CharField(max_length=20,null=True,blank=True)

    father = models.CharField(max_length=20,null=True,blank=True)
    mother = models.CharField(max_length=20,null=True,blank=True)
    present_address = models.CharField(max_length=400,null=True,blank=True)
    permanent_address = models.CharField(max_length=400,null=True,blank=True)

    blood_group = models.CharField(max_length=3,choices=BLOOD_GRP_CHOICES,null=True,blank=True)
    institutional_background = models.CharField(max_length=100,null=True,blank=True)
    background_club_Activities = models.CharField(max_length=250,null=True,blank=True)
    competitions = models.CharField(max_length=250,null=True,blank=True)

    DisplayFields = ['name','college_roll','year']
    SearchFields = ['name','college_roll','year','admission_serial','serial','transection_id','email','contact_number','father','mother','institutional_background']
    FilterFields = ['year']

    def __str__(self):
        return f'{self.name} ({self.college_roll})'
    
    class Meta:
      ordering = ['serial','-year',]
