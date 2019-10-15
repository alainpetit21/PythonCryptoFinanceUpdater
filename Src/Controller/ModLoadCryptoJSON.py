# This example uses Python 2.7 and the python-request library.

from Src.Controller.config import config
from Src.Model.ModelFacade import ModelFacade

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class ModLoadCryptoJSON:

    def __init__(self):
        self.url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        # self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        self.parameters = {
            'symbol': None,
            'convert': 'CAD'
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': config.mAPIKey
        }
        self.session = None

        self.parameters['symbol']= ModelFacade().get_all_currencies_string()

    def execute(self):
        self.session = Session()
        self.session.headers.update(self.headers)

        try:
            response = self.session.get(self.url, params=self.parameters)
            ModelFacade().import_JSON_quotes(response.text)
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


        dict_full_result= ModelFacade().get_all_results_quotes()

        for currency in ModelFacade().get_all_currencies_list():
            value = dict_full_result['data'][currency]['quote']['CAD']['price']
            ModelFacade().set_formatted_quote(currency, value)
