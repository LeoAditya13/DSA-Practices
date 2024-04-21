def Fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(3))

'''def check_even_list(num_list):
    for number in num_list:
        if number % 2 ==0:
            return True
        else:
            pass
    return False 
print(check_even_list([2,3,5,7,9]))'''

'''work_hours=(('Rohan',800),('Rohit',700),('Rahul',400),('Kishan',600))
def employee_check(work_hours):
    current_max=0
    employee_of_month=''
    for employee,hours in work_hours:
        if hours > current_max:
            current_max=hours
            employee_of_month=employee
        else:
            pass
    return(employee_of_month,current_max)

print(employee_check(work_hours))'''

'''def myfunc(word):
    result = ""
    for index, letter in enumerate(word):
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
    return result
word='aditya'
print(myfunc(word))'''