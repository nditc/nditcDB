from django.db import models
import uuid

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

class Member(models.Model):
    uniqueID = models.CharField(max_length=36,blank=True,default=uuid.uuid4())
    year = models.IntegerField()
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
