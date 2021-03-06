from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
#w momemncie logowania userowi zostaje przypisany randomowy string i sprawdzamy go z kazdym requestem

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer #zawsze kiedy bedzie put, patch or post bedzie spodziewal sie serializera
    #ktory zostal opisany w pliku serializer i bedzie sie spodziewal argumentu "name" z HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview}) #list or dictionary to be transformed easily to JSON

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data) #Pobranie serializera i przypisanie do niego danych z requestu

        if serializer.is_valid():
            name = serializer.validated_data.get('name') #tak pobieramy jakakolwiek zmienna z HalloSerializer
            message = f'Hello {name}' #f na poczatku to wtedy mozemy podac argument od razu w stringu
            return Response({'message': message}) #slownik zwracamy
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #uzywamy kodow statusu zeby od razu bylo
        #czytelnie

    def put(self, request, pk=None): #primary key w momencie kiedy bedziemy szukac obiektu po url key
        """Handle updating object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None): #primary key w momencie kiedy bedziemy szukac obiektu po url key
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None): #primary key w momencie kiedy bedziemy szukac obiektu po url key
        """Delete an object"""
        return Response({'method': 'DELETE'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request): #tak jak get w APIView
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message."""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) #mozemy dodac wiecej metod autentykacji dodajac dodatkowe klasy do tuple
    permission_classes = (permissions.UpdateOwnProfile,) #how to user gets permission to do certain things. user can be authenticated
                                                         #but dont have permission to call all of the methods
