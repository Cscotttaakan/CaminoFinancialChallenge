from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from .models import *

# Create your views here.


class CreateLoanApplicationView(generics.CreateAPIView):
    '''
    Basic idea is to flatten the nested dictionaries and join them to allow the
    update_or_create handle the heavy lifting.
    update_or_create handles the duplicate applications.
    '''
    def post(self, request):
        new_app_data = {**request.data['CFApplicationData'],**request.data['RequestHeader']}
        new_app,app_created = Application.objects.update_or_create(CFRequestId=new_app_data.pop('CFRequestId'),defaults=new_app_data)
        new_address = request.data['Business'].pop('Address')
        new_cashflow = {**request.data['Business'].pop('SelfReportedCashFlow'),**new_address}
        new_app.save()
        new_business,business_created = Business.objects.update_or_create(Name=request.data['Business'].pop('Name'),defaults={**request.data['Business'],**new_cashflow})
        new_business.App = new_app
        new_business.save()
        for owner in request.data['Owners']:
            new_owner,owner_created = Owner.objects.update_or_create(Name=owner.pop('Name'),DateOfBirth=owner.pop('DateOfBirth'),defaults={**owner,**owner.pop('HomeAddress')})
            new_owner.Business = new_business
            new_owner.save()

        return Response(status=200,data={'Updated' : str(app_created), 'AppID' : str(new_app.id)})

class StatusLoanApplicationView(generics.RetrieveAPIView):
    def get(self,request,*args,**kwargs):
        if 'id' in self.request.GET:
            try:
                app = Application.objects.get(id=self.request.GET['id'])
                return Response(status=200,data = {'Status' : app.Status})
            except Application.DoesNotExist:
                return Response(status=404, data = {'Error' : 'Object does not exist'})
        else:
            return Response(status=401,data = {'Error' : 'Missing query id'})
