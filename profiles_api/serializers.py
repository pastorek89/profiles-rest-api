from rest_framework import serializers

from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer): #podobny do basic ale ma duzo funkcjonalnosci ktore pomagaja
    """Serializes a user profile object"""                 #obslugiwac django rest framework

    class Meta: # zawsze w modelserializer konfigurujemy zeby wskazywal na szczegolny model w naszym projekcie
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')        #lista pol w naszym modelu ktore chcemy obslugiwac przez serializer
        extra_kwargs = {
            'password': {       #nie chcemy zeby haslo bylo nadpisane i retrieve. Tutaj pokazujemy ze chcemy wlasna konfiguracje do password
                'write_only': True,      #mozemy uzyc tylko do create i update, bez get
                'style': {'input_type': 'password'}         #gwiazdki albo kropki zamiast wpisywanego hasla
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user( #uzywa metody create_user z models UserProfilManager i tam jest setPassword dlatego
            email=validated_data['email'],              #bedzie podawane wczesniej i ustawiane jako hash, nie bedzie widoczne w programie
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
