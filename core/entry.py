import pandas as pd
from .models import Member
import os

def add(filename=26,year=2026):
    filename = str(os.getcwd())+f"\\core\\{filename}.csv"
    data = pd.read_csv(filename,dtype=str)
    # for col in data.columns:
    #     print(f"::{col}::")
    cout = 0
    for i in data.index:
        cout+=1
        # if i in [124,209,210,218]:
            #2025 ====>70
            #2024 ====>124,209,210,218
            # continue
        name = data['Name of Student'][i]
        contactNumber = data['Student Mobile'][i]
        clgRoll = data['Roll #'][i]
        sms_number = data['SMS Mobile'][i]
        print(f"\n{clgRoll} : Data fetched successfully")
        Member.objects.create(
            name=name,
            year=year,
            college_roll=clgRoll,
            contact_number=contactNumber,
            sms_number = sms_number
        )
        print(f'{clgRoll} : added to db successfully')

        # serial = data['Serial\nNo'][i]
        # transectionID = data['Transaction ID'][i]
        # name = data['Name of Student'][i]
        # father = data['Father\'s Name'][i]
        # mother = data['Mother\'s Name'][i]
        # admissionSerial = data['Admission Serial '][i]
        # clgRoll = data['College Roll'][i]
        # presentAddress = data['Present Address'][i]
        # permanentAddress = data['Permanent Address'][i]
        # contactNumber = data['Contact\nNumber'][i]
        # email = data['E-mail Address'][i]
        # bloodGrp = data['Blood \nGroup'][i]
        # institutionalBackground = data['Institutional \nBackground'][i]
        # backgroundClubActivities = data['Background of Club Activities'][i]
        # competitions = data['Name of competitions participated'][i]
        # try:
        #     Member.objects.create(
        #         year=year,
        #         serial=serial,
        #         transection_id=transectionID,
        #         admission_serial=admissionSerial,
        #         name=name,
        #         father=father,
        #         mother=mother,
        #         college_roll=clgRoll,
        #         present_address=presentAddress,
        #         permanent_address=permanentAddress,
        #         contact_number=contactNumber,
        #         email=email,
        #         blood_group=bloodGrp,
        #         institutional_background=institutionalBackground,
        #         background_club_Activities=backgroundClubActivities,
        #         competitions=competitions
        #     )
        # except Exception as e:
        #     print(f'{serial} ==> {e}')
        # print(serial)

# def nan():
#     Member.objects.filter(serial="nan").update(serial="")
#     Member.objects.filter(admission_serial="nan").update(admission_serial="")
#     Member.objects.filter(father="nan").update(father="")
#     Member.objects.filter(mother="nan").update(mother="")
#     Member.objects.filter(college_roll="nan").update(college_roll="")
#     Member.objects.filter(present_address="nan").update(present_address="")
#     Member.objects.filter(permanent_address="nan").update(permanent_address="")
#     Member.objects.filter(contact_number="nan").update(contact_number="")
#     Member.objects.filter(email="nan").update(email="")
#     Member.objects.filter(competitions="nan").update(competitions="")
#     Member.objects.filter(background_club_Activities="nan").update(background_club_Activities="")
#     Member.objects.filter(institutional_background="nan").update(institutional_background="")
"""
=====================2025======================================
        serial = data['Serial No.'][i]
        transectionID = data['Transection ID'][i]
        name = data['Name'][i]
        father = data['Father\'s Name'][i]
        mother = data['Mother\'s Name'][i]
        admissionSerial = data['Admission Serial'][i] #will be added
        clgRoll = data['College Roll'][i]
        presentAddress = data['Present Address'][i]
        permanentAddress = data['Permanent Address'][i]
        contactNumber = data['Contact Number'][i]
        email = data['E-Mail Address'][i]
        bloodGrp = data['Blood Group'][i]
        institutionalBackground = data['Institutional Background'][i]
        backgroundClubActivities = data['Background Club Activities'][i]
        competitions = data['Name of competitions you have participated'][i]
=======================2024================================
        serial = data['Serial\nNo'][i]
        transectionID = data['Transaction ID'][i]
        name = data['Name'][i]
        father = data['Father\'s Name'][i]
        mother = data['Mother\'s Name'][i]
        admissionSerial = data['Admission Serial '][i]
        clgRoll = data['College Roll'][i]
        presentAddress = data['Present Address'][i]
        permanentAddress = data['Permanent Address'][i]
        contactNumber = data['Contact\nNumber'][i]
        email = data['E-mail Address'][i]
        bloodGrp = data['Blood \nGroup'][i]
        institutionalBackground = data['Institutional \nBackground'][i]
        backgroundClubActivities = data['Background of Club Activities'][i]
        competitions = data['Name of competitions participated'][i]
"""
if __name__ == "__main__":
    add()