import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''测试name_function.py'''

    def test_first_last_name(self):
        '''能够正确处理向Janis Jopim这样的名字吗？'''
        formated_name = get_formatted_name('janis', 'jopim')
        self.assertEqual(formated_name,'Janis Jopim')

    def test_first_middle_last_name(self):
        '''能够正确处理像Wolfgang Amadeus Mozart这样的名字吗？'''
        formated_name = get_formatted_name('wolfgang', 'mozart', "amadeus")
        self.assertEqual(formated_name,'Wolfgang Amadeus Mozart')

unittest.main()