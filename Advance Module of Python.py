# COLLECTION MODULES
'''from collections import Counter 
mylist=[1,1,1,1,1,1,2,2,2,2,3,3,3,4,4,4,4,5,5,5,5,]
print(Counter(mylist))
sentence="How many times does each word show up in this sentence with a word"
print(Counter(sentence.split()))'''

# DEFAULT DICTIONARY 
'''from collections import defaultdict
d={"a":10}
print(d)
print(d["a"])
print(d["Wrong"]) #Will Give Error
c=(defaultdict(lambda:0))
c["Coorect"]=100
print(c["Coorect"])
print(c["Wrong Key!!"]) #Will Not Give Any Error''' 

# DATE-TIME MODULE
'''import datetime
mytime= datetime.time(2,20)
print(mytime)
today= datetime.date.today()
print(today.ctime())'''

#PRETTY TABLE
from prettytable import PrettyTable
table= PrettyTable()
table.add_column("Pokemon Name" , ["Pikachu", "Squirtle", "Charmender"])
table.add_column("Type", ["Electric","Water","Fire"])

table.align="l"

print(table)
