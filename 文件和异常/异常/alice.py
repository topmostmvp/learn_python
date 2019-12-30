filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print("sorry, the file " + filename + " dose not exist.")
else:
    #计算文件大致包含多少单词
    words = contents.split()
    num_words = len(words)
    print("the file " + filename + " has about " + str(num_words) + " words.")