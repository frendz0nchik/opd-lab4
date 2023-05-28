import unittest
from convert import app

class TestCurrencyConversion(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        

    def test_convert(self):
        data = {'currency_from': 'USD', 'currency_to': 'EUR', 'amount': '1'}
        result = self.app.post('/convert', data=data)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'<p>1.0 USD = 0.93 EUR</p>', result.data)

    def test_invalid_currency(self):
        data = {'currency_from': 'XXX', 'currency_to': 'USD', 'amount': '100'}
        result = self.app.post('/convert', data=data)
        self.assertEqual(result.status_code, 500)
        

if __name__ == '__main__':
    unittest.main()