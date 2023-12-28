from rest_framework import permissions,authentication
from .models import Member
from .serializers import MemberSerializer
from rest_framework.decorators import authentication_classes,permission_classes,api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404,get_list_or_404

# headers => 'Authorization':'Token ***********'
"""
////////////////get Token/////////////////////////
    method ===> POST
    url : https://foisal.pythonanywhere.com/api/v1/getToken/
    body ==> 'username': '***','password':'***'
"""
@api_view(['GET','POST','PATCH','PUT','DELETE'])
@authentication_classes([authentication.TokenAuthentication,authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def index(request,pk=None):
    if request.method == "GET":
        if pk != None:
            # fetch specific data
            member = get_object_or_404(Member,pk=pk)
            serializer = MemberSerializer(member)
        else:
            # fetch all data
            queryset = Member.objects.all()
            serializer = MemberSerializer(queryset,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Add data
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'PATCH' or request.method == 'PUT':
        if pk==None:
            return Response({'detail':'id or primary key is required!'})
        # Edit data
        qs = get_object_or_404(Member,pk=pk)
        serializer = MemberSerializer(data=request.data,instance=qs)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        if pk==None:
            return Response({'detail':'id or primary key is required!'})
        # delete data
        qs = get_object_or_404(Member,pk=pk)
        qs.delete()
        return Response({'detail':'deleted successfully!'})
    
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication,authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def year(request,year):
    # Fetch students by Year
    qs = get_list_or_404(Member,year=year)
    serializer = MemberSerializer(qs,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication,authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def runQuery(request):
    # run query directly
    # only applicable for the Table "CORE_MEMBER"
    # Fields: ID,YEAR,NAME,ADMISSION_SERIAL,COLLEGE_ROLL,SERIAL,CONTACT_NUMBER,EMAIL,TRANSECTION_ID,FATHER,MOTHER,PRESENT_ADDRESS,PERMANENT_ADDRESS,BLOOD_GROUP,INSTITUTOINAL_BACKGROUND,BACKGROUND_CLUB_ACTIVITIES,COMPETITIONS
    # DON'T CREATE ANY TABLE BY RUNNING QUERY
    # DON'T ADD ANY FIELD IN ANY TABLE BY RUNNING QUERY
    # Create Table and add fields by only using django Model
    # Get the id from https://foisal.pythonanywhere.com/api/v1/getID/
    # Don't use id as your wish
    try:
        objs = Member.objects.raw(request.data['query'])
        serializer = MemberSerializer(objs,many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'detail':str(e)})
    
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication,authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def getID(request):
    querySet = Member.objects.order_by('id')
    id = querySet[len(querySet)-1].id
    return Response({'detail':id})