from .models import Visitor
from serializers import VisitorSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView


class VisitorList(ListAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class VisitorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer

