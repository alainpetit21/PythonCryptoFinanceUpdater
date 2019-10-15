from Src.CrossCuttingConcerns.SingletonDecorator import SingletonDecorator
import json


class Results:
    pass

class Currencies:
    pass


@SingletonDecorator
class ModelFacade:

    def __init__(self):
        # For Module 1 - ModLoadCryptoJSON
        self.list_all_currencies= []
        self.dict_results_quotes = None
        self.dict_results_quotes_formated = {}

        # For Module 2 - ModLoadKMyMoneyXML
        self.str_filename_kMyMoney = None
        self.dict_kMyMoney_quotes_latest = {}

    def clear_all(self):
        self.list_all_currencies.clear()

    def add_currency(self, str_currency):
        self.list_all_currencies.append(str_currency)

    def get_all_currencies_string(self):
        str_all_currencies = ""

        for item in self.list_all_currencies:
            str_all_currencies= str_all_currencies + item + ','

        str_all_currencies= str_all_currencies[:-1]
        return str_all_currencies

    def get_all_currencies_list(self):
        return self.list_all_currencies

    def import_JSON_quotes(self, str_json):
        self.dict_results_quotes= json.loads(str_json)

    def set_formatted_quote(self, key, price):
        self.dict_results_quotes_formated[key]= price

    def get_formatted_quote(self, key):
        return self.dict_results_quotes_formated[key]

    def get_results_quotes_element(self, key):
        return self.dict_results_quotes[key]

    def get_all_results_quotes(self):
        return self.dict_results_quotes

    def add_KMyMoneyFile(self, str_filename):
        self.str_filename_kMyMoney = str_filename

    def get_KMyMoneyFile(self):
        return self.str_filename_kMyMoney

    def set_latest_KMyMoneyFile_quote(self, key, price):
        self.dict_kMyMoney_quotes_latest[key]= price
