# ======================================================================================================================
# main.py : entry point script for this example

# ======================================================================================================================
# importing internal modules
from Src.Controller.AppPythonCryptoFinanceUpdater import AppPythonCryptoFinanceUpdater


if __name__ == "__main__":
    print("Hello AppPythonCryptoFinanceUpdater World")

    objApp = AppPythonCryptoFinanceUpdater()

    objApp.load()
    objApp.main()
