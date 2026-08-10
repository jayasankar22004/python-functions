class Playlist:
    def __init__(self,l=[]):
        self.l=l
    def __len__(self):
        return len(self.l)
    def __add__(self, other):
        if other.endswith(".mp3"):
            self.append(other)
        else:
            print("only mp3 songs can be added.")
            return self
    def __contains__(self,other):
        return other in self.l
p1=Playlist()
p2=Playlist()
p1=p1+jaya.mp3
p1=p1+sunflower.mp3
p2=p2+hello.mp3
p2=p2+vikram.dsl
print(p1)
print(p2)

