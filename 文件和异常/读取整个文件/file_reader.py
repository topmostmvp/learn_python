with open("pi_digits.txt") as file_object: #with在不需要访问文件后将其关闭
    contents = file_object.read()
    print(contents.rstrip())
    