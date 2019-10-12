from Src.CrossCuttingConcerns.App import App
from Src.Controller.ModLoadCryptoJSON import ModLoadCryptoJSON


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
        pass

    def main(self, param1=None):
        """ main Description : (public visibility) :
            The main function of this Applicaiton objet.
        """
        ModLoadCryptoJSON().execute()

