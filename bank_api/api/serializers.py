from rest_framework import serializers
from .models import *

class BankBranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model= BankBranches
        fields = ['ifsc','bank_id','branch','address','city','district','state','bank_name']