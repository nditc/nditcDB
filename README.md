<h1 align="center">NDITC Members Database</h1>

# Build-with
- Python
- Django
- Django-REST-Framework
- Django-Jazzmin
- Pandas

# How to use
```bash
git clone https://github.com/nditc/nditcDB.git
cd nditcDB
python -m pip install -r requirements.txt
python manage.py collectstatic
python manage.py runserver
```

# Functionalites
- [Admin Panel](#admin-panel)
- [Token Authentication](#token-authentication)
- [Fetch all Students data](#fetch-all-students-data)
- [Fetch Students data by year](#fetch-students-data-by-year)
- [Fetch data of a specific student](#fetch-data-of-a-specific-student)
- [Add Student data](#add-student-data)
- [Update Student data](#update-student-data)
- [Delete Student data](#delete-student-data)
- [Run query](#run-query)

# Admin Panel
  You can add , edit , delete , view student by logging in on [Admin Panel](https://foisal.pythonanywhere.com)
# Token Authentication
  - To get token,you have to post valid <b>username</b> and <b>password</b> in https://foisal.pythonanywhere.com/api/v1/getToken/ .It will return  a JSON response
   - To authenticate, the token key should be included in the Authorization HTTP header. The key should be prefixed by the string literal "Token", with whitespace separating the two strings. For example:
    ```
    {
      Authorization: 'Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
    }
    ```
  - You have to add authentication credentials to perform anything
# Fetch all Students data
  Send a <b>GET</b> request to https://foisal.pythonanywhere.com/api/v1/
# Fetch Students data by year
  Send a <b>GET</b> request to the server and add the year in the URL

  Example of URL : https://foisal.pythonanywhere.com/api/v1/year/2025/
# Fetch data of a specific student
  Send a <b>GET</b> request to the server and add the id of the student in the URL

  Example of URL : https://foisal.pythonanywhere.com/api/v1/3666/
# Add Student data
  Send a <b>POST</b> request with data to https://foisal.pythonanywhere.com/api/v1/

  Include data in the HTTP Body.For example:
  ```
  {
    year : 0000,
    name : '',
    admission_serial : '',
    college_roll : '',
    serial : '',
    contact_number : '',
    email : '',
    father : '',
    mother : '',
    present_address : ''
    permanent_address : ''
    blood_group : ''
    institutional_background : ''
    background_club_Activities : ''
    competitions : ''
  }
  ```
# Update Student data
  Send a <b>PUT/PATCH</b> request with updated data to the server and add the id of the student in the URL . Include updated data in the HTTP Body

  Example of URL : https://foisal.pythonanywhere.com/api/v1/3666/
# Delete Student data
  Send a <b>DELETE</b> request to the server and add the id of the student in the URL

  Example of URL : https://foisal.pythonanywhere.com/api/v1/3666/
# Run query
  - You can run query only for the Table named <b>CORE_MEMBER</b>
  - The fields of the Table <b>CORE_MEMBER</b> are :
    - ID
    - YEAR
    - NAME
    - ADMISSION_SERIAL
    - COLLEGE_ROLL
    - SERIAL
    - CONTACT_NUMBER
    - EMAIL
    - TRANSECTION_ID
    - FATHER
    - MOTHER
    - PRESENT_ADDRESS
    - PERMANENT_ADDRESS
    - BLOOD_GROUP
    - INSTITUTOINAL_BACKGROUND
    - BACKGROUND_CLUB_ACTIVITIES
    - COMPETITIONS
  - <h4>DON'T CREATE ANY TABLE OR ADD ANY FIELD IN ANY TABLE BY RUNNING QUERY WITH THIS.</h4>
  - Create Table and add fields by only using django Model
  - You have to post the query in https://foisal.pythonanywhere.com/api/v1/query/ . Include the post data in the HTTP Body. For example:
  ```
  {
    query : 'SELECT * FROM CORE_MEMBER'
  }
  ```
  - When adding new data , you have to get id from https://foisal.pythonanywhere.com/api/v1/getID/ and use it as the id for the student. Don't put id as your wish.

  <b>Note</b> : Running query with this is not recommended . It may cause unusual internal errors.