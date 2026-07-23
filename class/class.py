#car
class Car:
    fuel_type='Petrol'
    def __init__ (self,ma,m,y,p):
        self.make=ma
        self.model=m
        self.year=y
        self.price=p
    def display(self):
        print(self.make,self.model,self.year,self.price)
c1=Car(ma='tata',m='punch',y=2024,p=1500000)
c2=Car(ma='mahindra',m='suv',y=2020,p=1300000)
c1.display()
c2.display()
#


