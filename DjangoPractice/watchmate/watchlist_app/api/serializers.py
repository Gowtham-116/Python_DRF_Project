from rest_framework import serializers
from watchlist_app.models import Watchlist,StreamPlatform,Review

# class StreamSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model=StreamPlatform
#         fields='__all__'
 
class ReviewSerializer(serializers.ModelSerializer):
    reviewer=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Review
        exclude=('watchlist',)
        #   fields='__all__'    

class WatchlistSerializer(serializers.ModelSerializer):
    reviews=ReviewSerializer(many=True,read_only=True)
    class Meta:
        model=Watchlist
        fields='__all__'
        #fields=['f1','f2']
        #exclude=['f3']
        
class StreamSerializer(serializers.HyperlinkedModelSerializer):
    #'watchlist is the related name given for foreignkey var in model 
    
    #watchlist=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='movie-detail')
    #watchlist=serializers.StringRelatedField(many=True,read_only=True)
    
    class Meta:
        model=StreamPlatform
        fields='__all__'
    watchlist=WatchlistSerializer(many=True,read_only=True)
        

    # def validate(self,data):
    #     if data['name']==data['description']:
    #         raise serializers.ValidationError('Name and Desc cant be same')
    #     else:
    #         return data
        
    # def validate_name(self,value):
    #     if len(value)<2:
    #         raise serializers.ValidationError('Name length cant be <2')
    #     else:
    #         return value
     

# class MovieSerialzer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     name=serializers.CharField()
#     description=serializers.CharField()
#     active=serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.description=validated_data.get('description',instance.description)
#         instance.active=validated_data.get('active',instance.active)
#         instance.save()
#         return instance