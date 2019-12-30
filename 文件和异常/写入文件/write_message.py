"""
写入模式在写入之前将清空文件，如果想在后面添加使用附加模式
"""
filename = 'programming.txt'

with open(filename, "w") as file_objct:  # r读取模式， w写入模式， a附加模式， r+读写和写入， 默认只读
    file_objct.write('I love programming.\n')
    file_objct.write('I love creating new games.\n')