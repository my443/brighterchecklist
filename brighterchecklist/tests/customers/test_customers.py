from django.test import TestCase
from django.http import HttpResponse, HttpRequest
from customers.views_customer_signup import *
from customers.models import Customer
from django import forms
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test.client import RequestFactory
from django.urls import reverse

class TestCustomers(TestCase):
    def setUp(self) -> None:
        ####################################################
        # This Section has to be here because of messages.
        # https://code.djangoproject.com/ticket/17971
        ####################################################
        request = RequestFactory()
        setattr(request , 'session', 'session')
        messages = FallbackStorage(request)
        setattr(request , '_messages', messages)
        request = HttpRequest()
        #####################################################

        factory = RequestFactory()
        data = {'message': 'A test message', 'emailAddress': 'test@test.org'}
        self.request = factory.post('/edit/1', data)

        setattr(self.request , 'session', 'session')
        messages = FallbackStorage(self.request)
        setattr(self.request , '_messages', messages)
        # self.request = HttpRequest()

        # self.request.POST['emailAddress'] = 'test@test_email.com'
        self.returnPage = new_customer_signup(self.request)
        #
        self.new_customer = Customer()
        self.new_customer.email = 'test@test_email.com'
        self.new_customer.save()

    ## A couple of sample tests to make sure testing is working ok.
    def test_this_will_pass(self):
        self.assertEqual('test', 'test')
    #
    # def test_something(self):
    #     self.assertEqual(something_to_test(), 'hello world')

    ##################################################
    ## New Customer Sign Up Tests
    ##################################################

    def test_returns_HTTPResponse(self):
        """Test that the response is an HTTPResponse"""
        returnPage = new_customer_signup(self.request)

        self.assertIsInstance(self.returnPage, HttpResponse)

    def test_new_customer_response_is_200(self):
        """You have to post the email address which comes from the home page."""

        data = {
            'emailAddress': 'test@test_email.com'
        }

        response = self.client.post('/customer/new/', data)
        self.assertEqual(response.status_code, 302)

    def test_customer_signup_success(self):
        # Simulate a POST request with valid data
        response = self.client.post(reverse('new_customer'), {'emailAddress': 'test@example.com'})

        # Check that the response redirects to 'home'
        self.assertRedirects(response, reverse('home'))

    def test_customer_is_added(self):
        # # Check that a new customer and user are created
        for customer in Customer.objects.all():
            print (customer.email)
        self.assertEqual(Customer.objects.count(), 1)

    def test_user_is_added(self):
        self.assertEqual(User.objects.count(), 1)

    # def test_that_you_cant_duplicate_customer_email(self):
    #     factory = RequestFactory()
    #     data = {'message': 'A test message', 'emailAddress': 'test@test.org'}
    #     self.request = factory.post('/edit/1', data)
    #
    #     setattr(self.request , 'session', 'session')
    #     messages = FallbackStorage(self.request)
    #     setattr(self.request , '_messages', messages)

