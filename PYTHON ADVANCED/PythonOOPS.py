#Creation of class

class Student():
    def __init__(self,name,age,marks,gpa):
        self.name = name
        self.age = age
        self.marks = marks #Attributes
        self.gpa = gpa
        
x = Student("Advaith",20, 90, 4.0)
y = Student("Achyuth", 21, 95, 4.0)
print(x)
print(y)
print(x.name)
print(y.name)
print(x.age)

class Agent():
    origin = "USA"
    def __init__(me, id, height, weight):
        me.id = id
        me.height = height
        me.weight = weight
        
x = Agent("001", 6.1, 180)
print(x.origin)
print(x.height)
print(x.weight)
print(x.id)
#--------------------------------------------------------------------------
#Methods

class Circle():
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return Circle.pi * (self.radius**2)
    def perimeter(self):
        return 2 * Circle.pi * self.radius
    
x = Circle(5)
print(x.area())
print(x.perimeter())
#--------------------------------------------------------------------------
#Inheritance

class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def hello(self):
        print("Hello I am " + self.firstname + " " + self.lastname)
        
    def report(self):
        print("Nice to meet you!")
        
x = Person("Advaith", "R Pai")
x.hello()
x.report()

class Agent(Person):
    def reveal(self, passcode):
        if passcode == 123:
            print("I am a secret agent!")
        else:
            self.report()
        
x = Person("Advaith", "R Pai")
x.reveal()
#--------------------------------------------------------------------------
#Special Methods

mylist = [1,2,3]
print(mylist)
print(len(mylist))

class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return "Title: " + self.title + " Author: " + self.author + " Pages: " + str(self.pages)
    
    def __len__(self):
        return self.pages
        

mybook = Book("Python", "Advaith", 200)
print(mybook)
print(len(mybook))
