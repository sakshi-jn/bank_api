from django.shortcuts import render
from rest_framework import  status
from rest_framework.response import  Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import BankBranchesSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django_filters import filters,FilterSet
import  django_filters

# Create your views here.
class BankFilter(django_filters.FilterSet):

    class Meta:
        model = BankBranches
        fields = ('bank_name','city')

    @property
    def qs(self):
        parent = super().qs
        author = getattr(self.request,'bank_name','city')

        return parent.filter(bank_name=bank_name) \
            | parent.filter(city= city)


class BankDetails(generics.ListAPIView):
    #ifsc = filters.CharFilter('ifsc')
    #bank_name = filters.CharFilter('bank_name')
    #city = filters.CharFilter('city')
    queryset = BankBranches.objects.all()
    serializer_class = BankBranchesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ifsc','bank_name', 'city']
    #filters_fields=('bank_name','city')
    filters_class= BankFilter


