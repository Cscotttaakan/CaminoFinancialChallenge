from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from rest_framework.response import Response

from .views import *
from .models import *

import json
import os


class CreateApplicationViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def tearDown(self):
        Application.objects.all().delete()
        User.objects.all().delete()

    def testCreate(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path,'sample.json'), 'r') as json_file:
            request_params = json.load(json_file)
        create_url = reverse('loans:createapp')
        resp = self.client.post(create_url,json.dumps(request_params),content_type='application/json')
        print(resp.status_code)
        self.assertTrue(resp.status_code==200)

class StatusApplicationViewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser', password='password')
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def tearDown(self):
        Application.objects.all().delete()
        User.objects.all().delete()

    def testCreate(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path,'sample.json'), 'r') as json_file:
            request_params = json.load(json_file)
        create_url = reverse('loans:createapp')
        resp = self.client.post(create_url,json.dumps(request_params),content_type='application/json')
        appid = resp.data['AppID']
        self.assertTrue(resp.status_code==200)

        create_url = reverse('loans:status')
        resp = self.client.get(create_url,data={'id' : appid})
        self.assertTrue(resp.data['Status'] == 'Pending')


