class Books:
    total_books=0
    def __init__(self,n,a):
        self.name=n
        self.author=a
        Books.total_books+=1
    @classmethod
    def creation(cls,n,a):
        if(len(n)>=5):
            return cls(n,a)
        else:
            print("title is too short")
    @classmethod
    def update(cls,nt):
        cls.total_books=nt
        print(f"total_books:{cls.total_books}")
cls=Books
b1=Books.creation("The Author's Pov","Author")
b1.update(30)
