class Book:
    total=0
    def __init__(self,t,a):
        self.title=t
        self.author=a
        Book.total+=1
    @staticmethod
    def is_valid(t):
        return len(t)>3
    @classmethod
    def from_string(cls,book_str):
        t,a=book_str.split("-")
        if cls.is_valid(t):
            b=Book(t,a)
            return b
        else:
            print("Invalid Title")
b1=Book.from_string("hi-bye")
if b1:
    print(b1.title,b1.author,sep="\n")
else:
    print("nothing in the object")


