import unittest
from ex1 import city
from city_function2 import city

class TestCities (unittest.TestCase):

    def test_city_country(self):
        self.assertEqual(city('Россия', 'Волгоград'), 'Россия, Волгоград', "Все не файн")
        # self.assertTrue(cities('Россия', 'Волгоград'), 'Россия , Волгоград')

if __name__ == 'main':
    unittest.main()