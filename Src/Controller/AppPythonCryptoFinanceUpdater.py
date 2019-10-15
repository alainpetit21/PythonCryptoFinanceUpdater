from Src.CrossCuttingConcerns.App import App
from Src.Controller.ModLoadCryptoJSON import ModLoadCryptoJSON
from Src.Controller.ModLoadKMyMoneyXML import ModLoadKMyMoneyXML
from Src.Model.ModelFacade import ModelFacade


class AppPythonCryptoFinanceUpdater(App):
    def __init__(self):
        """ __init__ Description : (public visibility) :
            Constructor methods that will create this object. I does not do a lot but, overload the BaseClass
            construction call and initialization the class attributes for this instance.
        """
        super().__init__("AppPythonCryptoFinanceUpdater")

    def load(self):
        """ load Description : (public visibility) :
            Method that is called directly after the creation of the object. Its purpose is to do all loading that is
            beside initial initialization.
        """
        # Model for ModuleLoadCryptoJSON
        ModelFacade().add_currency("BTC")
        ModelFacade().add_currency("BCH")
        ModelFacade().add_currency("ETH")
        ModelFacade().add_currency("LTC")
        ModelFacade().add_currency("MIOTA")
        ModelFacade().add_currency("CEL")

        # Model for ModLoadKMyMoneyXML
        ModelFacade().add_KMyMoneyFile("/home/apetit/Documents/Alain Petit/Others/finances.xml")



    def main(self, param1=None):
        """ main Description : (public visibility) :
            The main function of this Applicaiton objet.
        """
        ModLoadCryptoJSON().execute()
        ModLoadKMyMoneyXML().execute()
