# # Single or Basic Inheritance

# # Base class
# class Parent:
#     def __init__(self, name):
#         self.name= name


#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived class
# class Child(Parent):
#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of Child
# child = Child("Alice")
# child.greet()     # Output: Hello, my name is Alice
# child.play()    # Output: Alice is playing

#----------------------------------------------------------------------

# # Multilevel inheritance

# # Base class
# class Grandparent:
#     def __init__(self, name):
#         self.name =name

#     def tell_story(self):
#         print(f"{self.name} tells a story.")

# # Intermediate class
# class Parent(Grandparent):
    
#     def work(self):
#         print(f"{self.name} is working.")

# # Derived class
# class Child(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of child
# child = Child("Charlie")
# child.tell_story()      # Output: Charlie tells a story
# child.work()        # Output: Charlie is working
# child.play()      # Output: Charlie is playing
        
#------------------------------------------------------------------

# # Hierarchial Inheritance

# # Base class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived class 1
# class Child1(Parent):

#     def play(self):
#         print(f"{self.name} is playing")

# # Derived class 2
# class Child2(Parent):
    
#     def study(self):
#         print(f"{self.name} is studying.")

# # Create instance of Child1 and Child2
# child1 = Child1("Dave")
# child2 = Child2("Eve")

# child1.greet()      # Output: Hello, my name is Dave.
# child1.play()       # Output: Dave is playing.

# child2.greet()      # Output: Hello, my name is Eve.
# child2.study()       # Output: Eve is studying.

#------------------------------------------------------------------------------

# Multiple Inheritance (Diamond Problem)

# # Common base class
# class A:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello from A, {self.name}.")

# # Intermediate Class 1
# class B(A):

#     def greet(self):
#         print(f"Hello from B, {self.name}.")
#         super().greet()

# # Intermediate Class 2
# class C(A):
#     def greet(self):
#         print(f"Hello from C, {self.name}.")
#         super().greet()

# # Derived class
# class D(B,C):

#     def greet(self):
#         print(f"Hello from D, {self.name}.")
#         super().greet()

# # Create an instance of D
# d = D("Frank")
# d.greet()

# # Output:
# # Hello from D, Frank.
# # Hello from B, Frank.
# # Hello from C, Frank.
# # Hello from A, Frank.

#--------------------------------------------------------------------0

# Hybrid Inheritance

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")

# Intermediate Class 1 (Hierarchial)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

# Intermediate Class 2 (Multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying.")

# Derived class (Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self, name):
        Mammal.__init__(self, name)     # Explicitly calling the constructor

    def nocturnal(self):
        print(f"{self.name} is nocturnal.")

# Create an instance of Bat
bat = Bat("Bruce")
bat.sound()     
bat.feed()
bat.fly()
bat.nocturnal()