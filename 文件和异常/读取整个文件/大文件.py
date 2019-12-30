filename = 'pi_digitss.txt'

with open(filename) as file_object:
    lines = file_object.readlines()  #readlines()从文件中读取每一行并储存在一个列表中

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))