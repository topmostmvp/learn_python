filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  #readlines()从文件中读取每一行并储存在一个列表中

for line in lines:
    print(line.rstrip())

print(lines)  #结果为['3.1415926535\n', '  8979323846\n', '  2643383279']