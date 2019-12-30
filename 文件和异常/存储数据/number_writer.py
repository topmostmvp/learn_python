import json

numbers = [2, 3, 5, 7, 11, 13]

filename = "numbers.json"
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)  #第一个实参是数据，第二个实参是用来存数据的文件对象
