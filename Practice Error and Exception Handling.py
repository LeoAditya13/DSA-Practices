# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.
def ask():
    while True:
        try:
            result = int(input("Input an Integer : "))
        except:
            print("An Error Occured!! Please Try Again \n")
            continue
        else:
            print("Thank You, Your Number Squared is : ",result**2)
            break 
ask()
