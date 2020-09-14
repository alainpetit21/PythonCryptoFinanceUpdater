# This example uses Python 2.7 and the python-request library.

from Src.Controller.config import config
from Src.Model.ModelFacade import ModelFacade

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class ModLoadCryptoJSON:

    def __init__(self):
        """ __init__ Description : (public visibility) :
            Constructor methods that will create this object. Initialization the attributes for this instance.
        """
        # Depending if I am testing or not I would use the sandbox link
        # self.url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        self.url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

        # All parameters for the requests session. Note that config.mAPIKey is my own personnal key,
        # To use on your own terms, create a config.py and config class with this class level attribute
        self.parameters = {
            'symbol': None,
            'convert': 'CAD'
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': config.mCoinMarketAPIKey
        }
        self.session = None

        # Overloading the 'symbol' with all currencies saved in the Model by the App
        self.parameters['symbol']= ModelFacade().get_all_currencies_string()

    def execute(self):
        """ execute Description : (public visibility) :
            The one function to call for this module functionality. Execute the loading of JSON using Coinmarketcap
            public API
        """
        #method local attribute initialization
        dict_full_result= None

        # Prepare the requests session
        self.session = Session()
        self.session.headers.update(self.headers)

        try:
            # Launch it and pass the resulting converted JSON to python
            response = self.session.get(self.url, params=self.parameters)
            dict_full_result= json.loads(response.text)

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            # TODO : better error catching
            print(e)

        # The resulting Dic countains way too much information for our need. Strip everything and keep just the
        # Symbol : price key pair.
        for currency in ModelFacade().get_all_cryptocurrencies_list():
            value = dict_full_result['data'][currency]['quote']['CAD']['price']
            ModelFacade().set_formatted_quote(currency, value)
