from django.shortcuts import render
from django.http import JsonResponse

from watchlist_app.models import Watchlist,StreamPlatform,Review
from watchlist_app.api.serializers import WatchlistSerializer,StreamSerializer,ReviewSerializer
from watchlist_app.api.permissions import IsAdminOrReadOnly,ReviewUserOrReadOnly


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status,mixins,generics,viewsets
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated


# Create your views here.

class Reviewcreate(generics.CreateAPIView):

    serializer_class=ReviewSerializer  
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        watchlist=Watchlist.objects.get(pk=pk)
        # reviewer=self.request.user
        review_user=self.request.user
        print(review_user)
        review_qs=Review.objects.filter(watchlist=watchlist,reviewer=review_user)
        if review_qs.exists():
            raise ValidationError("you have already reviewed this movie")
        
        if watchlist.count_rating==0:
            watchlist.avg_rating=serializer.validated_data['rating']
        else:
            watchlist.avg_rating=(watchlist.avg_rating+serializer.validated_data['rating'])/2
        
        watchlist.count_rating+=1
        watchlist.save()
        
        serializer.save(watchlist=watchlist,reviewer=review_user)
        

class Reviewlist(generics.ListCreateAPIView):
    #queryset=Review.objects.all() 
    #overriding query set as above one is giving all values
    serializer_class=ReviewSerializer
    # permission_classes=[IsAuthenticated]
    
    #overriding query set as above one is giving all values
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return Review.objects.filter(watchlist=pk)
     

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer 
    permission_classes=[ReviewUserOrReadOnly]  

# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class=ReviewSerializer
#     def get(self,request,*args, **kwargs):
#         return self.retrieve(request,*args, **kwargs)    

# class Reviewlist(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Review.objects.all()
#     serializer_class= ReviewSerializer
#     def get(self,request,*args, **kwargs):
#         return self.list(request,*args, **kwargs)
    
#     def post(self,request,*args, **kwargs):
#         return self.create(request,*args, **kwargs)

class MovielistAV(APIView):
    permission_classes=[IsAdminOrReadOnly]  

    def get(self,request):
        movies=Watchlist.objects.all()
        serializer= WatchlistSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) #comes from serializer return object
        else:
            return Response(serializer.errors)
        
class MoviedetailAV(APIView):
    permission_classes=[IsAdminOrReadOnly]  

    def get(self,request,pk):
        try:
            movies=Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error':'Movie Not Found'},status=404)
        serializer= WatchlistSerializer(movies)
        return Response(serializer.data)
    
    def post(self,request,pk):
        movies=Watchlist.objects.get(pk=pk)
        serializer=WatchlistSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    def delete(self,request,pk):
        movies=Watchlist.objects.get(pk=pk)         
        movies.delete()
        return Response({'Post deleted'},status=status.HTTP_204_NO_CONTENT)

class StreamplatformVS(viewsets.ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]  

    queryset=StreamPlatform.objects.all()
    serializer_class=StreamSerializer

# class StreamingAV(APIView):
#     def get(self,request):
#         platform=StreamPlatform.objects.all()
#         serializer=StreamSerializer(platform,many=True,context={'request':request})
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=StreamSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
class StreamdetailAV(APIView):
    permission_classes=[IsAdminOrReadOnly]  

    def get(self,request,pk):
        try:
            movies=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Movie Not Found'},status=404)
        serializer= StreamSerializer(movies,context={'request':request})
        return Response(serializer.data)
    
    def post(self,request,pk):
        movies=StreamPlatform.objects.get(pk=pk)
        serializer=StreamSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    def delete(self,request,pk):
        movies=StreamPlatform.objects.get(pk=pk)         
        movies.delete()
        return Response({'Post deleted'},status=status.HTTP_204_NO_CONTENT)
        
    
# @api_view(['GET','POST'])
# def movielist(request):
    
#     if request.method=='GET': 
#         movies=Movie.objects.all()
#         serializer= MovieSerialzer(movies,many=True)
#         return Response(serializer.data)
    
#     if request.method=='POST':
#         serializer=MovieSerialzer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data) #comes from serializer return object
#         else:
#             return Response(serializer.errors)
        

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,pk):
#     if request.method=='GET': 
#         try:
#             movies=Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error':'Movie Not Found'},status=404)
#         serializer= MovieSerialzer(movies)
#         return Response(serializer.data)
    
#     if request.method=='PUT':
#         movies=Movie.objects.get(pk=pk)
#         serializer=MovieSerialzer(movies,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
            
#     if request.method=='DELETE':
#         movies=Movie.objects.get(pk=pk)         
#         movies.delete()
#         return Response({'sdfgfgdfrs'},status=status.HTTP_204_NO_CONTENT)


    
    
    