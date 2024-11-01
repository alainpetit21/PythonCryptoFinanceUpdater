from Src.Controller.ModApplyCryptoCurrencyPrice import ModApplyCryptoCurrencyPrice
from Src.CrossCuttingConcerns.App import App
from Src.Controller.ModLoadCryptoJSON import ModLoadCryptoJSON
from Src.Controller.ModPrintAllCryptoHistoryPrice import ModPrintAllCryptoHistoryPrice
from Src.Model.ModelFacade import ModelFacade


class AppPythonCryptoFinanceUpdater(App):
    def __init__(self):
        """ __init__ Description : (public visibility) :
            Constructor methods that will create this object. I does not do a lot but, overload the BaseClass
            construction call and initialization the attributes for this instance.
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
        ModelFacade().add_currency("BTG")
        #ModelFacade().add_currency("BCD")
        ModelFacade().add_currency("ETH")
        ModelFacade().add_currency("LTC")
        # ModelFacade().add_currency("MIOTA")
        ModelFacade().add_currency("IOTA")
        ModelFacade().add_currency("CEL")
        ModelFacade().add_currency("HNT")
        ModelFacade().add_currency("XYO")

        # ModelFacade().add_security("0P0000715P.TRT")
        # ModelFacade().add_security("0P0000715V.TRT")
        # ModelFacade().add_security("0P000072TQ.TRT")
        # ModelFacade().add_security("HQH")
        # ModelFacade().add_security("HQL")
        # ModelFacade().add_security("TCT-UN.TRT")

        # ModelFacade().add_security("QBTC.TO")
        # ModelFacade().add_security("QETH.UN.TO")
        # ModelFacade().add_security("VAB.TO")
        # ModelFacade().add_security("VUN.TO")
        # ModelFacade().add_security("XEC.TRT")
        # ModelFacade().add_security("XEF.TRT")
        # ModelFacade().add_security("MCM103")

        # Model for ModLoadKMyMoneyXML
        # ModelFacade().add_KMyMoneyFile("/home/alain/Documents/Alain Petit/Others/finances.xml")
        # ModelFacade().add_KMyMoneyFile("/home/alain/Documents/Alain Petit/Others/finances.xml.bak")
        # ModelFacade().add_KMyMoneyFile("/home/apetit/Documents/Alain Petit/Others/finances.xml")
        # ModelFacade().add_KMyMoneyFile("/home/apetit/Documents/Alain Petit/Others/financesTest.xml")
        ModelFacade().add_KMyMoneyFile("D:\\Work\\AlainPetit\\Others\\finances.xml")

    def main(self, param1=None):
        """ main Description : (public visibility) :
            The main function of this Applicaiton objet.
        """
        ModLoadCryptoJSON().execute()
        ModPrintAllCryptoHistoryPrice().execute()
        ModApplyCryptoCurrencyPrice().execute()
