def add(n1,n2):
    print(n1+n2)
num1=20
num2= int(input("Please Enter Your Number : "))
print(add(num1,num2)) # Will Give this error ---> unsupported operand type(s) for +: 'int' and 'str'
print("Something Wrong!!") #This Will Never Execute'''

try:
    result=10+"10"
except:
    print("Hey It Looks like you aren't adding correctly!!")
else:
    print("Add went well!!")

print(result)

'''def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a Number : "))
        except: 
            print("WHOOPS! That is not a Number.")
            continue
        else:
            print("Yes Thank You")
            break   
        finally:
            print("I'm Going to ask you again! \n")

ask_for_int()''' 




