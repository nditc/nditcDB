from rest_framework import permissions,authentication
from .models import Member
from .serializers import MemberSerializer
from rest_framework.decorators import authentication_classes,permission_classes,api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404,get_list_or_404

@api_view(['GET','POST','PATCH','PUT','DELETE'])
@authentication_classes([authentication.TokenAuthentication,authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def index(request,pk=None):
    if request.method == "GET":
        if pk != None:
            member = get_object_or_404(Member,pk=pk)
            serializer = MemberSerializer(member)
        else:
            queryset = Member.objects.all()
            serializer = MemberSerializer(queryset,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'PATCH' or request.method == 'PUT':
        if pk==None:
            return Response({'detail':'id or primary key is required!'})
        qs = get_object_or_404(Member,pk=pk)
        serializer = MemberSerializer(data=request.data,instance=qs)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == 'DELETE':
        if pk==None:
            return Response({'detail':'id or primary key is required!'})
        qs = get_object_or_404(Member,pk=pk)
        qs.delete()
        return Response({'detail':'deleted successfully!'})
    
@api_view(['GET'])
@authentication_classes([authentication.TokenAuthentication,authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def year(request,year):
    qs = get_list_or_404(Member,year=year)
    serializer = MemberSerializer(qs,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication,authentication.SessionAuthentication])
@permission_classes([permissions.IsAuthenticated])
def runQuery(request):
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