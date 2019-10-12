# This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from Src.Controller.config import config

class ModLoadCryptoJSON:

    def __init__(self):
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.parameters = {
            'start': '1',
            'limit': '5000',
            'convert': 'USD'
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': config.mAPIKey
        }
        self.session = None

    def execute(self):
        self.session = Session()
        self.session.headers.update(self.headers)

        try:
            response = self.session.get(self.url, params=self.parameters)
            data = json.loads(response.text)
            print(data)

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
