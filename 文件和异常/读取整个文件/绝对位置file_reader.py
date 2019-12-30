file_path = "/media/topmost/topmost/linux/VScode/python/文件和异常/读取整个文件/pi/pi_digits.txt"
with open(file_path) as file_object:
    content = file_object.read()
    print(content)