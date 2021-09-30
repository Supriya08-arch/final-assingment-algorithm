from django.test import RequestFactory, TestCase
from .views import latest_jobs
from .views import Recruiter,index

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




