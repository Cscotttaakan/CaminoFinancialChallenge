from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.urls import reverse

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

    def tearDown(self):
        Application.objects.all().delete()

    def testCreate(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path,'sample.json'), 'r') as json_file:
            print(json_file)
            request_params = json.load(json_file)
            create_url = reverse('loans:createapp')
            resp = self.client.post(
                    url=create_url,
                    data=request_params,
                    )
            self.assertTrue(resp.status_code==200)
