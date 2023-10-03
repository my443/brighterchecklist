from django.test import TestCase
import os

# os.environ["DJANGO_SETTINGS_MODULE"] = "..brighterchecklist.settings"

class TestCustomers(TestCase):
    # settings.configure()
    ## A couple of sample tests to make sure testing is working ok.
    def test_this_will_pass(self):
        self.assertEqual('test', 'test')