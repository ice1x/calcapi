from rest_framework.views import APIView
from rest_framework.response import Response


class Calc(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, pk1, pk2, format=None):
        return Response(pk1+pk2)
