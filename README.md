## **Project: Theme Park Adventure System**
---

### **Introduction to Object-Oriented Programming (OOP)**

Object-Oriented Programming (OOP) is a paradigm that structures software into reusable "objects" that represent real-world entities. Key principles of OOP include **encapsulation**, **inheritance**, **polymorphism**, and **abstraction**.

---

### **Key Concepts for this Project**

#### 1. **Encapsulation**
Encapsulation involves bundling data (attributes) and methods (functions) together and restricting access to some details. In Python, we use **private attributes** (prefixed with `__`) to hide data from direct access, ensuring changes happen only through controlled methods.

**Example**:  
```python
class Ride:
    def __init__(self, name, duration):
        self.__name = name  # Private attribute
        self.__duration = duration  # Private attribute
    
    def get_details(self):  # Public method
        return f"Ride Name: {self.__name}, Duration: {self.__duration} minutes"
```

---

#### 2. **Polymorphism**
Polymorphism allows the same operation to behave differently for different classes or objects. This is often achieved by **method overriding**. Subclasses redefine methods from their parent class, tailoring behavior to their needs.

**Example**:
```python
class Attraction:
    def description(self):
        return "A fun attraction at the theme park."

class RollerCoaster(Attraction):
    def description(self):  # Overriding parent method
        return "A thrilling roller coaster ride with loops and drops!"

class FerrisWheel(Attraction):
    def description(self):  # Overriding parent method
        return "A relaxing ferris wheel ride with scenic views."
```

---

### **Project: Theme Park Adventure System**

Your task is to design a **Theme Park Adventure System** using OOP principles. The system will manage attractions, staff, and visitors, using encapsulation and polymorphism effectively.

---

### **Step 1: Define the Base Class**

#### **1. Attraction Class (Base Class)**  
A base class for all attractions at the theme park.

**Attributes**:  
- `__name` (private): Name of the attraction.  
- `__capacity` (private): Maximum number of people the attraction can hold.  

**Methods**:  
- `__init__(name, capacity)`: Initializes the attraction's name and capacity.  
- `get_details()`: Returns a string summarizing the attraction details:  
  `"Attraction: [name], Capacity: [capacity]"`.  
- `start()`: A generic message, `"The attraction is starting."`  

---

### **Step 2: Create Subclasses**

#### **2. ThrillRide Class (inherits from Attraction)**  
Represents high-adrenaline rides like roller coasters.  

**Attributes**:  
- Inherits all attributes from `Attraction`.  
- `__min_height` (private): Minimum height required to ride (in cm).  

**Methods**:  
- `__init__(name, capacity, min_height)`: Initializes all attributes, including the new one.  
- `start()`: Overrides `start()` to return: `"Thrill Ride [name] is now starting. Hold on tight!"`  
- `is_eligible(height)`: Checks if a person meets the height requirement.  

---

#### **3. FamilyRide Class (inherits from Attraction)**  
Represents family-friendly rides like carousels.  

**Attributes**:  
- Inherits all attributes from `Attraction`.  
- `__min_age` (private): Minimum age to ride.  

**Methods**:  
- `__init__(name, capacity, min_age)`: Initializes all attributes, including the new one.  
- `start()`: Overrides `start()` to return: `"Family Ride [name] is now starting. Enjoy the fun!"`  
- `is_eligible(age)`: Checks if a person meets the age requirement.  

---

### **Step 3: Define Other Classes**

#### **4. Staff Class (Base Class)**  
A base class for all theme park staff.

**Attributes**:  
- `__name` (private): Staff name.  
- `__role` (private): Role of the staff member (e.g., "Operator").  

**Methods**:  
- `__init__(name, role)`: Initializes the staff details.  
- `work()`: A generic message, `"Staff [name] is performing their role: [role]."`  

---

#### **5. Visitor Class**  
A class representing visitors at the theme park.

**Attributes**:  
- `__name` (private): Visitor's name.  
- `__age` (private): Visitor's age.  
- `__height` (private): Visitor's height in cm.  

**Methods**:  
- `__init__(name, age, height)`: Initializes the visitor details.  
- `ride(attraction)`: Tries to ride an attraction. Checks eligibility using the appropriate method (`is_eligible`) from `ThrillRide` or `FamilyRide`.  

---

### **Step 4: Tasks and Challenges**

---

#### **Task 1: Create Classes**

1. Define the `Attraction` base class with appropriate encapsulation.  
2. Define the `ThrillRide` and `FamilyRide` subclasses, overriding the `start()` method and including specific eligibility checks.  
3. Define the `Staff` and `Visitor` classes, using encapsulation for all attributes.  

---

#### **Task 2: Demonstrate Encapsulation**

1. Create a `ThrillRide` object (e.g., "Dragon Coaster", capacity 20, min height 140 cm).  
2. Create a `FamilyRide` object (e.g., "Merry-Go-Round", capacity 30, min age 4).  
3. Create a `Visitor` object and attempt to ride both attractions, demonstrating eligibility checks.  

---

#### **Task 3: Demonstrate Polymorphism**

1. Create multiple attractions (e.g., a thrill ride and a family ride).  
2. Call the `start()` method on both objects and observe the behavior.  

---

### **Extension Task: Park Management System**

Develop a **Park Management System** with the following additional features:

#### 1. **Staff Management**  
Add a `Manager` subclass to `Staff` with attributes:  
- `__team` (private): A list of `Staff` objects reporting to the manager.  

**Methods**:  
- `add_staff(staff)`: Adds a `Staff` object to the manager's team.  
- `get_team_summary()`: Lists all staff names and roles in the team.  

#### 2. **Advanced Attraction Features**  
Add a `status` attribute to `Attraction` to track whether it is open or closed.  

**Methods**:  
- `open_attraction()`: Marks the attraction as "Open".  
- `close_attraction()`: Marks the attraction as "Closed".  
- Modify `start()` to check the status before starting the ride.

#### 3. **Visitor Activities**  
Enhance the `Visitor` class with a `ride_history` attribute to track the rides they’ve taken.  

**Methods**:  
- `view_history()`: Returns a list of rides the visitor has experienced.  

---

**Example Output**:
```python
visitor = Visitor("Alice", 10, 130)
coaster = ThrillRide("Dragon Coaster", 20, 140)

print(coaster.start())  # Output: "Thrill Ride Dragon Coaster is now starting. Hold on tight!"
visitor.ride(coaster)  # Output: "Alice is not eligible for Dragon Coaster."

carousel = FamilyRide("Merry-Go-Round", 30, 4)
visitor.ride(carousel)  # Output: "Alice is enjoying the Merry-Go-Round!"
visitor.view_history()  # Output: ["Merry-Go-Round"]
```