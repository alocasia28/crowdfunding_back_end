from rest_framework.views import APIView
from rest_framework.response import Response
from .models import  Project, Pledge 
from .serializers import  ProjectSerializer, PledgeSerializer, ProjectDetailSerializer 
from django.http import Http404
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly
from django.db.models import Sum

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, 
                    status=status.HTTP_201_CREATED
            )
        
        return Response (
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    
            


    #I have added this in as my custom OK code. If something breaks, check this. If that works, add in a bad error for the
class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request,project)
            # return project
            return Project.objects.get(pk=pk)
        #modifying the get object model to include a permissions check. So the view will apply its registered permissions whenever a user performs an action on a model instance
        except Project.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        project = self.get_object(pk)
        project.update_total(project_id=pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project, 
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                    status=status.HTTP_200_OK
            )
        
    def delete(self, request, pk, format=None):
        deleted = self.get_object(pk)
        deleted.delete()
        return Response(status=status.HTTP_200_OK)
    #using a 200 response so in the front end I can display this with a nice message?
        
    #This is what Atlas and I did. 
    def total_pledges(self, request, pk):
        total = Pledge.objects.filter(project=pk).aggregate(Sum('amount'))
        return Response(total,status=status.HTTP_200_OK)
    
                
class PledgeList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #this requires a user to be authenticated so we know who submitted the pledge. A user is not able to change their pledge after submitting. 
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

#My understanding of ListCreateAPIView and RetrieveUpdateDestoryAPIView is that they're a quicker way

# class CommentListAPI(generics.ListCreateAPIView):
    
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Comment.objects.filter(visible=True)
#     serializer_class = CommentSerializer 

# class CommentDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
#     queryset = Comment.objects.filter(visible=True)
#     serializer_class = CommentSerializer