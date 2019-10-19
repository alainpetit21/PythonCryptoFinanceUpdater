# This example uses Python 2.7 and the python-request library.

from Src.Model.ModelFacade import ModelFacade
from lxml import etree


class ModLoadKMyMoneyXML:

    def __init__(self):
        """ __init__ Description : (public visibility) :
            Constructor methods that will create this object. Initialization the attributes for this instance.
        """
        self.objDOM= None

    def execute(self):
        """ execute Description : (public visibility) :
            The one function to call for this module functionality. Loads and interpret the KMyMoney file from disk
        """

        # Open the KMyMoney file and create a DOM from the XML
        with open(ModelFacade().get_KMyMoneyFile()) as in_file:
            self.objDOM = etree.parse(in_file.buffer)

        # For all the currencies in the model, find the category for this pricepair using XPATH
        for currency in ModelFacade().get_all_currencies_list():
            for res_price_pair in self.objDOM.xpath("//*[@to='CAD' and @from='"+ currency +"']"):

                # Find the latest price quote (in format 1234 / 1000 to give 1.234, kmymoney weird way of manipulating
                # floating points)
                for price in list(res_price_pair):
                    str_quote = price.get("price")
                    data_quote = str_quote.split('/')
                    left_value = data_quote[0]
                    right_value = data_quote[1]

                    last_value = int(left_value) / int(right_value)

                    # Tell the model to keep this data
                    ModelFacade().set_latest_KMyMoneyFile_quote(currency, last_value)
                    print(currency + "=" + str(last_value))
