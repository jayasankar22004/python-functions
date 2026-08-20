class Rapido:
    usernames = {}
    def __init__(self, name, username, age, gender, psd):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = psd
        self.logged = False
        self.ride_list = []
        Rapido.usernames[username] = self
    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")
        while True:
            username = input("Enter your Username: ")

            if username in cls.usernames:
                print("Username already registered. Try another one")
                continue
            break
        psd = input("Enter Your Password: ")
        age = input("Enter your Age: ")
        gender = input("Enter your Gender (Male/Female): ")
        return cls(name, username, age, gender, psd)
    def login(self):
        if self.logged:
            print("Already logged in")
        else:
            user = input("Enter your username: ")
            password = input("Enter your password: ")
            if user == self.username and password == self.password:
                self.logged = True
                print("Logged in Successfully")
            else:
                print("Invalid details")
    def logout(self):
        if self.logged:
            self.logged = False
            print("Logged out Successfully")
        else:
            print("Already logged out")
    def book_ride(self):
        if self.logged:
            pickup = input("Enter Pickup Location: ")
            destination = input("Enter Destination: ")
            distance = float(input("Enter Distance in KM: "))
            fare = distance * 15
            ride = {
                "pickup": pickup,
                "destination": destination,
                "distance": distance,
                "fare": fare
            }
            self.ride_list.append(ride)
            print("\nRide Booked Successfully")
            print("Pickup      :", pickup)
            print("Destination :", destination)
            print("Distance    :", distance, "KM")
            print("Fare        : ₹", fare)
        else:
            print("Not logged in")
    def cancel_ride(self):
        if self.logged:
            if len(self.ride_list) > 0:
                ride = self.ride_list.pop()
                print("\nRide Cancelled Successfully")
                print("Pickup      :", ride["pickup"])
                print("Destination :", ride["destination"])
            else:
                print("No rides available")
        else:
            print("Not logged in")
    def profile(self):
        if self.logged:
            print("\n----- PROFILE -----")
            print("Name     :", self.name)
            print("Username :", self.username)
            print("Age      :", self.age)
            print("Gender   :", self.gender)
            print("Rides    :", len(self.ride_list))
        else:
            print("Not logged in")

r1 = Rapido.signup()
r2 = Rapido.signup()
r1.login()
r1.book_ride()
r1.book_ride()
r1.profile()
r1.cancel_ride()
r1.logout()