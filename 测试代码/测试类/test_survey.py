import unittest
from survey import AnnoymousSurvey

class TestAnnoymousSurvey(unittest.TestCase):
    '''针对AnnoymousSurvey类的测试'''

    def setUp(self):
        '''
        创建一个调查对象和一组答案，供使用的测试方法使用
        '''
        question = "What language did you first learn to speak?"
        self.my_survey = AnnoymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Spnish']

    def test_store_single_response(self):
        '''测试单个答案会被妥善的保存'''

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_response(self):
        '''测试三个答案会被妥善的保存'''

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()