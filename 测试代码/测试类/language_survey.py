from survey import AnnoymousSurvey

#定义一个问题，并创建一个表示调查的AnnoymousSurvy对象
question = "What's your favorite language?"
my_survey = AnnoymousSurvey(question)

#显示问题并存储答案
my_survey.show_question()
print("Enter 'q' at any time to quit")

while True:
    response = input("Language:")
    if response == 'q':
        break
    my_survey.store_response(response)

#显示调查结果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
