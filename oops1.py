# initiate a class
class employee:
    # special method/magic method/dunder method - contructor
    def __init__(self):
        print("Started executing attibutes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")
    
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")


# Create an object/instance of the class
sam = employee()

# printing the attributes
# print(sam.id)

# calling a method
# sam.travel("Kerala")

print(type(sam))