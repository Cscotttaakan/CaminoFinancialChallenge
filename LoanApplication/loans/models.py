from django.db import models

#Create your models here.
#Business
#Owner
#LoanApplication

class Application(models.Model):
    RequestedLoanAmount = models.FloatField(default=0)
    StatedCreditHistory = models.IntegerField(default=0)
    LegalEntityType = models.CharField(max_length=20)
    FilterID = models.IntegerField(default=0)
    CFRequestId = models.IntegerField(default=0)
    RequestDate = models.DateTimeField(auto_now=False)
    CFApiUserId = models.IntegerField(default=0,null=True)
    CFApiPassword = models.CharField(max_length=100,null=True)
    IsTestLead = models.BooleanField(default=False)
    Status = models.CharField(max_length=100,default='Pending')

    def __str__(self):
        return str(self.CFRequestId)


class Business(models.Model):
    App = models.ForeignKey(Application, related_name='app', on_delete=models.CASCADE, null = True)
    Name = models.CharField(max_length=100)
    AnnualRevenue = models.FloatField(default=0)
    MonthlyAverageBankBalance = models.FloatField(default=0)
    MonthlyAverageCreditCardVolume = models.FloatField(default=0)
    TaxID = models.CharField(max_length=10)
    Phone = models.CharField(max_length=20)
    NAICS = models.CharField(max_length=5)
    HasBeenProfitable = models.BooleanField(default=False)
    HasBankruptedInLast7Years = models.BooleanField(default=False)
    InceptionDate = models.DateTimeField(auto_now=False)
    Address1 =  models.CharField(max_length=200)
    Address2 = models.CharField(max_length=200,null=True)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=20)
    Zip = models.CharField(max_length=5)

    Updated = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self):
        return self.Name

class Owner(models.Model):
    Name = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    DateOfBirth = models.DateTimeField(auto_now=False)
    SSN = models.CharField(max_length=9)
    PercentageOfOwnership = models.FloatField(default=0)
    Address1 =  models.CharField(max_length=200)
    Address2 = models.CharField(max_length=200,null=True)
    City = models.CharField(max_length=100)
    State = models.CharField(max_length=20)
    Zip = models.CharField(max_length=5)
    HomePhone = models.CharField(max_length=20,null=True)
    Business = models.ForeignKey(Business, related_name='Owners', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Name


