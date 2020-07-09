from django.db import models

# Create your models here.
class BankBranches(models.Model):

    ifsc= models.CharField(max_length= 11 , blank= False, null= False, unique=True)
    bank_id = models.BigIntegerField()
    branch = models.CharField(max_length=80)
    address = models.TextField()
    city = models.CharField(max_length= 50)
    district = models.CharField(max_length= 50)
    state = models.CharField(max_length= 30)
    bank_name = models.CharField(max_length= 100)

    def __str__(self):
        return "IFSC: {}  BANK: {}".format(self.ifsc, self.bank_name)



