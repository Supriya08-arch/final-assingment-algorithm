from django.test import RequestFactory, TestCase
from .views import latest_jobs
from .views import Recruiter,index, add_job, job_list, latest_jobs, user_latestjobs, applied_candidatelist, recruiter_all
from django.core.mail import send_mail
from django.conf import settings

from django import setup
from django.test.testcases import TestCase, Client
from django.urls import reverse, resolve

from django.test import RequestFactory, TestCase



# Create your tests here.

class JobTest(TestCase):

    def test_home_page_status_code(self):
        print("testing the status code")
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    # testing the recruiter object
    def test_all(self):
        print("testing all field")
        abc = Recruiter.objects.all()
        self.assertEqual(abc.count(),0)
     # testing aspects of index page
    def test_environment_set_in_context(self):
        print("testing images")
        request = RequestFactory().get('/static/images/')
        view = index(request)




# Testing of user_login
class TestViews(TestCase):
    def setUp(self):
        self.user_login = reverse("user_login")

    def test_user_login(self):
        response = self.client.get(self.user_login)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_login.html')

# testing  urls
class TestUrls(TestCase):
    def test_add_job_url(self):
        url = reverse('add_job')
        self.assertEqual(resolve(url).func, add_job)

    def test_job_list_url(self):
        url = reverse('job_list')
        self.assertEqual(resolve(url).func, job_list)

    def test_latest_jobs_url(self):
        url = reverse('latest_jobs')
        self.assertEqual(resolve(url).func, latest_jobs)

    def test_user_latestjobs_url(self):
        url = reverse('user_latestjobs')
        self.assertEqual(resolve(url).func, user_latestjobs)

    def test_applied_candidatelist_url(self):
        url = reverse('applied_candidatelist')
        self.assertEqual(resolve(url).func, applied_candidatelist)

    def test_recruiter_all_url(self):
        url = reverse('recruiter_all')
        self.assertEqual(resolve(url).func, recruiter_all)














