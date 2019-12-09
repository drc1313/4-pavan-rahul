from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db import models
from nhsee.models.judge_model import judge
from django.urls import reverse


class JudgeTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password=''
        )

        self.judge = judge.objects.create(
            judge_id='AA027',
            fname='1',
            lname='Judge',
        )

    def test_string_representation(self):
        judge = self.judge
        self.assertEqual(judge,"judge: 1")
