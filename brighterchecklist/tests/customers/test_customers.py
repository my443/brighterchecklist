from django.test import TestCase
from django.http import HttpResponse, HttpRequest
from customers.views import *
from django import forms

class TestCustomers(TestCase):
    def setUp(self) -> None:
        self.request = HttpRequest()
        self.request.POST['emailAddress'] = 'test@test_email.com'
        self.returnPage = new_customer_signup(self.request)

        self.new_customer = Customer()
        self.new_customer.email = 'test@test_email.com'

    # ## A couple of sample tests to make sure testing is working ok.
    # def test_this_will_pass(self):
    #     self.assertEqual('test', 'test')
    #
    # def test_something(self):
    #     self.assertEqual(something_to_test(), 'hello world')

    ##################################################
    ## New Customer Sign Up Tests
    ##################################################

    def test_returns_HTTPResponse(self):
        """Test that the response is an HTTPResponse"""
        # returnPage = new_customer_signup(self.request)

        self.assertIsInstance(self.returnPage, HttpResponse)

    def test_new_customer_response_is_200(self):
        """You have to post the email address which comes from the home page."""

        data = {
            'emailAddress': 'test@test_email.com'
        }

        response = self.client.post('/customer/new/', data)
        self.assertEqual(response.status_code, 200)

    def test_form_for_new_customer_is_form_object(self):
        form = generate_new_customer_form(self.new_customer)

        self.assertIsInstance(form, forms.Form)

    def test_form_has_email_element(self):
        form = generate_new_customer_form(self.new_customer)
        html_string = '<input type="text" name="email" value="test@test_email.com" class="form-control" readonly="readonly" required id="id_email">'

        self.assertIn(html_string, str(form))

    def test_form_has_email_address_element_again(self):
        form = generate_new_customer_form(self.new_customer)
        html_string = '<input type="text" name="email" value="test@test_email.com" class="form-control" readonly="readonly" required id="id_email">'

        self.assertEqual(str(form['email']), html_string)