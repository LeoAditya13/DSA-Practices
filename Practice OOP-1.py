# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.
'''class Line():
    
    def __init__(self,coor1,coor2):
        self.coor1=coor1
        self.coor2=coor2
    
    def distance(self):
        x1,y1=self.coor1
        x2,y2=self.coor2
        return ((x2-x1)**2 + (y2-y1)**2)**0.5
    
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return (y2-y1)/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)
li = Line(coordinate1,coordinate2)
 
print(li.distance())
print(li.slope())'''

class Account():
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def __str__(self):
        return f"Account Owner = {self.owner} \n Account Balance = ${self.balance}"

    def deposit(self,dep_amt):
        self.balance += dep_amt
        print("Deposit Accepted")
    
    def withdrawl(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print("Withdrawl Accepted")
        else:
            print("Funds Unavailable!")
acct1= Account("Aditya",100)
print(acct1)

acct1.deposit(50) 

acct1.withdrawl(500) 

