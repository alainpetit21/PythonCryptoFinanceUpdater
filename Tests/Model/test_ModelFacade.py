import unittest
from Src.Model.ModelFacade import ModelFacade


class ModelFacadeTest(unittest.TestCase):
    obj_model_facade = None


    def setUp(self):
        self.obj_model_facade = ModelFacade()

    def tearDown(self):
        self.obj_model_facade.clear_all()

    def test_create_default(self):
        self.assertEqual("", self.obj_model_facade.get_all_currencies_string())

    def test_create_one_currency(self):
        self.obj_model_facade.add_currency("BTC")
        self.assertEqual("BTC", self.obj_model_facade.get_all_currencies_string())

    def test_create_one_security(self):
        self.obj_model_facade.add_security("BTC")
        self.assertEqual("BTC", self.obj_model_facade.get_all_securities_string())

    def test_create_lot_currencies(self):
        self.obj_model_facade.add_currency("ABC")
        self.obj_model_facade.add_currency("DEF")
        self.obj_model_facade.add_currency("GHI")
        self.obj_model_facade.add_currency("JKL")
        self.obj_model_facade.add_currency("MNO")
        self.obj_model_facade.add_currency("PQR")
        self.obj_model_facade.add_currency("STU")
        self.obj_model_facade.add_currency("VWX")
        self.obj_model_facade.add_currency("YZ")
        self.assertEqual("ABC,DEF,GHI,JKL,MNO,PQR,STU,VWX,YZ", self.obj_model_facade.get_all_currencies_string())

    def test_create_lot_securities(self):
        self.obj_model_facade.add_security("ABC")
        self.obj_model_facade.add_security("DEF")
        self.obj_model_facade.add_security("GHI")
        self.obj_model_facade.add_security("JKL")
        self.obj_model_facade.add_security("MNO")
        self.obj_model_facade.add_security("PQR")
        self.obj_model_facade.add_security("STU")
        self.obj_model_facade.add_security("VWX")
        self.obj_model_facade.add_security("YZ")
        self.assertEqual("ABC,DEF,GHI,JKL,MNO,PQR,STU,VWX,YZ", self.obj_model_facade.get_all_securities_string())
