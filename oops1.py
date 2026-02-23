class Employee:
    #Special Function/Method, Megic Metho/Dunder Method- Constructor
    def __init__(self):
        print("Strating executing attributes/data")
        self.id= 123
        self.salary= 50000
        self.designation= "Software Development Engineer"
        print("Attribute/data have been initiated")

    def travel(self,destination):
        print("This travel method was called Manually")
        print(f"Employee is now travelling to {destination}")    
#Creating an object/instance of the class
sam=Employee()

#printing the attributes
#print(sam.id)

#Calling a Method
sam.travel("USA")

print(type(sam))