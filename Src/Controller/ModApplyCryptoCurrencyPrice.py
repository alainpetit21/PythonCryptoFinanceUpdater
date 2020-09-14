# This example uses Python 2.7 and the python-request library.

from Src.Model.ModelFacade import ModelFacade
from lxml import etree
from datetime import datetime


class ModApplyCryptoCurrencyPrice:

    def __init__(self):
        """ __init__ Description : (public visibility) :
            Constructor methods that will create this object. Initialization the attributes for this instance.
        """
        self.objDOM= None

    def execute(self):
        """ execute Description : (public visibility) :
            The one function to call for this module functionality. Add a new price pair quote to the XML and save the
            File
        """

        # Open the KMyMoney file and create a DOM from the XML
        with open(ModelFacade().get_KMyMoneyFile()) as in_file:
            self.objDOM= etree.parse(in_file.buffer)

        # Loop through from the currencies list saved in the model, and for each add an PRICE entry for the latest quote
        for cryptocurrency in ModelFacade().get_all_cryptocurrencies_list():
            for res_price_pair in self.objDOM.xpath("//*[@to='CAD' and @from='"+ cryptocurrency + "']"):
                # Creation of the PRICE node
                child_new_price = etree.SubElement(res_price_pair, "PRICE")
                child_new_price.set("source", "CryptoFinanceUpdater")

                # KMyMoney save quote as an equation (e.g. 100/20 for 5.0)
                # In our case, we shall always use the (int / 1000) format and save it to 3 decimal digit of precisions
                latest_price = int(ModelFacade().get_formatted_quote(cryptocurrency) * 1000)
                child_new_price.set("price", str(latest_price) + "/1000")

                # Date of that quote
                str_time= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                year = str_time[0:4]
                month = str_time[5:7]
                day = str_time[8:10]
                child_new_price.set("date", str(year) + "-" + str(month) + "-" + str(day))

                print("New price par " + cryptocurrency + " at " + str(latest_price/1000.0))


        # Convert the DOM to a string, and save it back to the file
        str_output = etree.tostring(self.objDOM, pretty_print=True)
        with open(ModelFacade().get_KMyMoneyFile(), 'wb') as out_file:
            out_file.write(str_output)
