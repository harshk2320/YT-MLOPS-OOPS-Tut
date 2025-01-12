# initiate a class
class employee:
    # special method/magic method/dunder method - contructor
    def __init__(self):
        # print(id(self))
        # print("Started executing attibutes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        # print("attributes/data have been initiated")
    
    def travel(self):
        print("This travel method was called manually")
        print(f"Employee is now travelling to delhi")


# Create an object/instance of the class
sam = employee()
# print(id(sam))
sam.name = "Sam Kumar"
print(sam.name)

# shaktiman = employee()
# print(id(shaktiman))

# printing the attributes
# print(sam.id)

# calling a method
# sam.travel()

# print(type(sam))