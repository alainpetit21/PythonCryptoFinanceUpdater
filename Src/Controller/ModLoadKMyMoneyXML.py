# This example uses Python 2.7 and the python-request library.

from Src.Model.ModelFacade import ModelFacade
from lxml import etree


class ModLoadKMyMoneyXML:

    def __init__(self):
        self.objDOM= None

    def execute(self):

        with open(ModelFacade().get_KMyMoneyFile()) as in_file:
            self.objDOM = etree.parse(in_file.buffer)

        lst_allCurrencies = ModelFacade().get_all_currencies_list()

        for currency in lst_allCurrencies:
            for res_price_pair in self.objDOM.xpath("//*[@to='CAD' and @from='"+ currency +"']"):

                for price in list(res_price_pair):
                    str_quote = price.get("price")
                    data_quote = str_quote.split('/')
                    left_value = data_quote[0]
                    right_value = data_quote[1]

                    last_value = int(left_value) / int(right_value)

                    ModelFacade().set_latest_KMyMoneyFile_quote(currency, last_value)
                    print(currency + "=" + str(last_value))
