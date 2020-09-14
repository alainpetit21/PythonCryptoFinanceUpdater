# This example uses Python 2.7 and the python-request library.

from Src.Controller.config import config
from Src.Model.ModelFacade import ModelFacade
from Src.Model.ModelFacade import ModelFacade
from lxml import etree
from datetime import datetime
import logging
from alpha_vantage.timeseries import TimeSeries
import time


class ModLoadCryptoJSON:

    def __init__(self):
        pass

    def doOneSecurity(self, security):
        logging.basicConfig(filename='example.log', level=logging.DEBUG)
        logging.basicConfig(format='%(asctime)-15s %(clientip)s %(user)-8s %(message)s')

        str_price = ""
        cpt_retry = 10

        while cpt_retry > 0:
            cpt_retry = cpt_retry - 1
            logging.info("One try to pull data ... {} remaining\n".format(cpt_retry))

            try:
                ts = TimeSeries(key=config.mAlphaVantageAPIKey, output_format='pandas')
                data, meta_data = ts.get_daily(symbol=security, outputsize='compact')
                str_price = data['4. close'][0]
                cpt_retry = 0
            except:
                logging.warning("ts.get_daily did not worked, trying ts.get_intraday\n")

                try:
                    ts = TimeSeries(key=config.mAlphaVantageAPIKey, output_format='pandas')
                    data, meta_data = ts.get_intraday(symbol=security, outputsize='compact')
                    str_price = data['4. close'][0]
                    cpt_retry = 0
                except ValueError as error:
                    logging.error("Because of the 5 / minute API called limit ?\n")
                except:
                    logging.error("ts.get_intraday failed Is it because of the 5 / minute API called limit ?\n")
                finally:
                    # Probably exceeded the API limit of 5 calls per minutes try again, recursively
                    str_price = "0.00"
                    time.sleep(60)

            return str_price

    def execute(self):
        # Open the KMyMoney file and create a DOM from the XML
        with open(ModelFacade().get_KMyMoneyFile()) as in_file:
            self.objDOM= etree.parse(in_file.buffer)

        # Loop through from the currencies list saved in the model, and for each add an PRICE entry for the latest quote
        for security in ModelFacade().get_all_securities_list():
            val = self.doOneSecurity(security)

            if val is not "0.00":
                print("Securities handling not working")