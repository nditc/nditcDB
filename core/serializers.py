from rest_framework import serializers
from .models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = (
            'id',
            'year',
            'name',
            'admission_serial',
            'college_roll',
            'serial',
            'contact_number',
            'email',
            'transection_id',
            'father',
            'mother',
            'present_address',
            'permanent_address',
            'blood_group',
            'institutional_background',
            'background_club_Activities',
            'competitions'
        )