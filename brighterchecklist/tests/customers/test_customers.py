from django.test import TestCase
from customers.views import something_to_test

class TestCustomers(TestCase):

    ## A couple of sample tests to make sure testing is working ok.
    def this_will_pass(self):
        self.assertEqual('test', 'test')

    def test_something(self):
        self.assertEqual(something_to_test(), 'hello world')

