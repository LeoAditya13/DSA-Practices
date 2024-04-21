class Animal():
    def __init__(self):
        print("Animal Created!!")
    def who_am_I(self):
        print("I am an Animal")
    def eat(self):
        print("I am Eating!!")

class Dog(Animal):      # Inheritance Method is used
    species="Mammal" #Class Object Attribute
    def __init__(self,breed,name):
        Animal.__init__(self) #Use of Inheritance 
        print("Dog Created!!")
        self.name=name
        self.breed=breed
    #Operations/Actions -----> Methods (To call Methods we have to use paranthesis)
    def bark(self):
        print(f"WOOF!! My Name is {self.name}") 

mydog=Dog(breed='Labrador',name='Tyson')

print(mydog.breed,mydog.name,mydog.species) #No Need to use Paranthesis
#print(mydog.who_am_I())
#print(mydog.bark()) #Use Paranthesis
#print(mydog.eat())


# Special Methods
'''class book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
        
    def __str__(self): # Use of Built in Function or Special Method 
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

mybook=book("Python Rocks!!","Jose",200)
print(mybook)
print(len(mybook))'''