import unittest
from Src.Model.ModelFacade import ModelFacade


class ModelFacadeTest(unittest.TestCase):
    obj_model_facade = None

    def setUp(self):
        self.obj_model_facade = ModelFacade()

    def tearDown(self):
        self.obj_model_facade.clear_all()

    def test_create_default(self):
        self.assertEqual(self.obj_model_facade.get_all_currencies_string(), "")

    def test_create_one_currencies(self):
        self.obj_model_facade.add_currency("BTC")
        self.assertEqual(self.obj_model_facade.get_all_currencies_string(), "BTC")

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
        self.assertEqual(self.obj_model_facade.get_all_currencies_string(), "ABC,DEF,GHI,JKL,MNO,PQR,STU,VWX,YZ")

    def test_json_import(self):
        self.obj_model_facade.import_JSON_quotes('{ "name":"John", "age":30, "city":"New York"}')
        self.assertEqual(self.obj_model_facade.get_results_quotes_element('name'), "John")
        self.assertEqual(self.obj_model_facade.get_results_quotes_element('age'), 30)
        self.assertEqual(self.obj_model_facade.get_results_quotes_element('city'), "New York")
