# This example uses Python 2.7 and the python-request library.

from Src.Model.ModelFacade import ModelFacade
from lxml import etree
from datetime import datetime


class ModCopyAndSaveKMyMoneyXML:

    def __init__(self):
        self.objDOM= None

    def execute(self):
        with open(ModelFacade().get_KMyMoneyFile()) as in_file:
            self.objDOM= etree.parse(in_file.buffer)

        lst_allCurrencies = ModelFacade().get_all_currencies_list()

        for currency in lst_allCurrencies:
            for res_price_pair in self.objDOM.xpath("//*[@to='CAD' and @from='"+ currency +"']"):
                print(res_price_pair)

                child_new_price = etree.SubElement(res_price_pair, "PRICE")
                child_new_price.set("source", "CryptoFinanceUpdater")

                latest_price = int(ModelFacade().get_formatted_quote(currency) * 1000)
                child_new_price.set("price", str(latest_price) + "/1000")

                str_time= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                year = str_time[0:4]
                month = str_time[5:7]
                day = str_time[8:10]
                child_new_price.set("date", str(year) + "-" + str(month) + "-" + str(day))


        str_output = etree.tostring(self.objDOM, pretty_print=True)

        with open(ModelFacade().get_KMyMoneyFile(), 'wb') as out_file:
            out_file.write(str_output)