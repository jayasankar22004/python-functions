def fun():
    name = input("enter your name:")
    age = int(input("enter your age"))
    course = input("enter your course")
    print(f"Name is,{name}\n Age is,{age}\n Course is,{course}")
while True:
    op=int(input("enter '1' to continue and '2' to exit"))
    if op==1:
        fun()
    else:
        break


