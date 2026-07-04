#nested functions
def add(x,y):
    def display(x,y):
        print(x,y)
    display(10,20)
add(10,20)