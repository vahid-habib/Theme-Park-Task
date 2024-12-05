class Attraction:
    def __init__(self, name, capacity):
        self._name = name
        self._capacity = capacity
        self._status = "Closed"  

    def get_details(self):
        print(f"Attraction: {self._name}, Capacity: {self._capacity}, Status: {self._status}")

    def open_attraction(self):
        self._status = "Open"

    def close_attraction(self):
        self._status = "Closed"

    def start(self):
        if self._status == "Open":
            print("The attraction is Starting")
        else:
            print("The attraction is closed and cannot start.")

class ThrillRide(Attraction):
    def __init__(self, name, capacity, minHeight):
        super().__init__(name, capacity)
        self._minHeight = minHeight

    def start(self):
        if self._status == "Open":
            print(f"Thrill Ride {self._name} is now starting. Hold on Tight!")
        else:
            print(f"Thrill Ride {self._name} is closed.")

    def isEligible(self, visitor):
        return visitor._height >= self._minHeight

class FamilyRide(Attraction):
    def __init__(self, name, capacity, minAge):
        super().__init__(name, capacity)
        self._minAge = minAge

    def start(self):
        if self._status == "Open":
            print(f"Family Ride {self._name} is now starting. Enjoy the Fun!")
        else:
            print(f"Family Ride {self._name} is closed.")

    def isEligible(self, visitor):
        return visitor._age >= self._minAge

class Staff:
    def __init__(self, name, role):
        self._name = name
        self._role = role

    def work(self):
        print(f"Staff {self._name} is performing their role: {self._role}")

class Manager(Staff):
    def __init__(self, name):
        super().__init__(name, "Manager")
        self._team = []

    def add_staff(self, staff):
        self._team.append(staff)

    def get_team_summary(self):
        for member in self._team:
            print(f"Name: {member._name}, Role: {member._role}")

class Visitor:
    def __init__(self, name, height, age):
        self._name = name
        self._height = height
        self._age = age
        self.ride_history = []  

    def ride(self, attraction):
        if attraction.isEligible(self):
            print(f"The Visitor {self._name} is now riding on {attraction._name}")
            self.ride_history.append(attraction._name)  
            attraction.start()  
        else:
            print(f"The Visitor {self._name} cannot ride on {attraction._name}")

    def view_history(self):
        return self.ride_history


danielCoaster = ThrillRide("Daniel Coaster", 30, 150)
mahdiRide = FamilyRide("Mahdi Ride", 10, 10)
vahid = Visitor("Vahid", 180, 16)

danielCoaster.open_attraction()  
vahid.ride(danielCoaster)  
vahid.ride(mahdiRide)  


manager = Manager("Katie")
staff1 = Staff("Alim", "Operator")
manager.add_staff(staff1)
manager.get_team_summary()


print("Ride History:", vahid.view_history())
