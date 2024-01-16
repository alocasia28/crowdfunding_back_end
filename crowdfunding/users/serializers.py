from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password':{'write_only':True}} 
        #serializer is looking at our model, we don't want it to share our passwords, we pass in a kwarg with extra info about how it should be serialized
        #this will send it to the model when a new user is created but will never bounce it back to the user
    def create(self, validated_data): #for other models, the default create method will work fine but passwords are a special case. 
        return CustomUser.objects.create_user(**validated_data) 