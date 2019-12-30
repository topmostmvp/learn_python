print("Giv me two number, and I'll divide them.\nEnter 'q' to quit/n")

while True:
    first_number = input("First number")
    if first_number == 'q':
        break
    second_number = input("Second number")
    if second_number == 'q':
        break
    else:
        try:
            answer = int(first_number)/int(second_number)
        except ZeroDivisionError:
            print("you can't divide by zreo!")
        else:
            print(answer)