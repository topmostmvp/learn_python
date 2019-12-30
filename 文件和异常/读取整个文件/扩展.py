filename = 'pi_digitss.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  #readlines()从文件中读取每一行并储存在一个列表中

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appeas in the third million digits of pi")
else:
    print('sorry')

