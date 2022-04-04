from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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


