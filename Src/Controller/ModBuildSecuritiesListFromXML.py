# This example uses Python 2.7 and the python-request library.

from Src.Model.ModelFacade import ModelFacade
from lxml import etree


class ModBuildSecuritiesListFromXML:

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
