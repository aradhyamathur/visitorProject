from .models import Visitor
from serializers import VisitorSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class VisitorList(ListCreateAPIView):

    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class VisitorDetail(RetrieveUpdateDestroyAPIView):

    serializer_class = VisitorSerializer
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        qs = Visitor.objects.filter(id=self.kwargs['pk'])
        return qs




