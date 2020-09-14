from Src.CrossCuttingConcerns.SingletonDecorator import SingletonDecorator


class Results:
    pass

class Currencies:
    pass


@SingletonDecorator
class ModelFacade:

    def __init__(self):
        # For Module 1 - ModLoadCryptoJSON
        self.list_all_currencies= []
        self.dict_results_quotes_formated = {}

        # For Module 2 - MOdPringAllCryptoHistoryPrice
        self.str_filename_kMyMoney = None
        self.dict_kMyMoney_quotes_latest = {}

        # For Module - ModLoadSecurities
        self.list_all_securities= []

    def clear_all(self):
        self.list_all_currencies.clear()
        self.list_all_securities.clear()

    def add_currency(self, str_currency):
        self.list_all_currencies.append(str_currency)

    def add_security(self, str_security):
        self.list_all_securities.append(str_security)

    def get_all_currencies_string(self):
        str_all_currencies = ""

        for item in self.list_all_currencies:
            str_all_currencies= str_all_currencies + item + ','

        str_all_currencies= str_all_currencies[:-1]
        return str_all_currencies

    def get_all_securities_string(self):
        str_all_securities = ""

        for item in self.list_all_securities:
            str_all_securities= str_all_securities + item + ','

        str_all_securities= str_all_securities[:-1]
        return str_all_securities

    def get_all_cryptocurrencies_list(self):
        return self.list_all_currencies

    def get_all_securities_list(self):
        return self.list_all_securities

    def set_formatted_quote(self, key, price):
        self.dict_results_quotes_formated[key]= price

    def get_formatted_quote(self, key):
        return self.dict_results_quotes_formated[key]

    def add_KMyMoneyFile(self, str_filename):
        self.str_filename_kMyMoney = str_filename

    def get_KMyMoneyFile(self):
        return self.str_filename_kMyMoney

    def set_latest_KMyMoneyFile_quote(self, key, price):
        self.dict_kMyMoney_quotes_latest[key]= price
