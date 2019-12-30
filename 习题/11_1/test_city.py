import unittest
from city_function import city_function

class TestCaseName(unittest.TestCase):

    def test_city_country(self):
        name = city_function('santiago', 'chile')
        self.assertEqual(name, 'Santiago, Chile')

unittest.main()