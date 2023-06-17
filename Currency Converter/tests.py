from flask_testing import TestCase
from flask import Flask
from your_flask_app import app

class CurrencyConverterTestCase(TestCase):

    def create_app(self):
        # Create a Flask app instance for testing
        app.config['TESTING'] = True
        return app

    def test_homepage(self):
        # Test the homepage (GET request)
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('form.html')
        
    def test_conversion(self):
        # Test the currency conversion (POST request)
        response = self.client.post('/convert', data={
            'currency_from': 'United States Dollar',
            'currency_to': 'Euro',
            'amount': '100'
        })
        self.assert200(response)
        self.assert_template_used('result.html')
        self.assert_context('amount', '100')
        self.assert_context('currency_from', 'United States Dollar')
        self.assert_context('currency_to', 'Euro')


