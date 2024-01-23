#====================================================================================================================#
# a program to make a simple calculator:
# Design a simple calculator with basic arithmetic operations.
# Prompt the user to input two numbers and an operation choice.
# Perform the calculation and display the result.
#====================================================================================================================#


#====================================================================================================================#
                                            # Functions Definition #
#====================================================================================================================#

# a function to make the required operation on the input numbers 
def makeOperation(num1,num2,op):
    result = 0
    if(op == '+'):
        result = num1+num2
    elif(op == '-'):
        result = num1-num2
    elif(op == '*'):
        result = num1*num2
    elif(op == '/'):
        result = num1/num2
    else:
    	print("Invalid input operation!")
    	return
    return result


# a function the required operation 
def chooseOperation():
    print("add  ==> +")
    print("sub  ==> -")
    print("mul  ==> *")
    print("div  ==> /")
    print("Quit ==> Q")
    userChoice = input("Enter your choice : ")
    while(userChoice != '+' and userChoice != '-' and userChoice != '*' and userChoice != '/' and userChoice != 'Q'):
    	userChoice = input("Enter Valid Operation : ")
    return userChoice
    
# main code
def main():
	while True:
		# get the required operation from the user 
		userChoice = chooseOperation()
		if(userChoice == '+'):
			# get the two numbers from the user 
			num1 = int(input("Enter num1 : "))
			num2 = int(input("Enter num2 : "))
			# calculate the required operation
			result = makeOperation(num1,num2,userChoice)
			# display the result
			print("==================")
			print("Result : ",result)
			print("==================")
		if(userChoice == '-'):
			# get the two numbers from the user 
			num1 = int(input("Enter num1 : "))
			num2 = int(input("Enter num2 : "))
			# calculate the required operation
			result = makeOperation(num1,num2,userChoice)
			# display the result
			print("==================")
			print("Result : ",result)
			print("==================")
		if(userChoice == '*'):
			# get the two numbers from the user 
			num1 = int(input("Enter num1 : "))
			num2 = int(input("Enter num2 : "))
			# calculate the required operation
			result = makeOperation(num1,num2,userChoice)
			# display the result
			print("==================")
			print("Result : ",result)
			print("==================")
		if(userChoice == '/'):
			# get the two numbers from the user 
			num1 = int(input("Enter num1 : "))
			num2 = int(input("Enter num2 : "))
			# calculate the required operation
			result = makeOperation(num1,num2,userChoice)
			# display the result
			print("==================")
			print("Result : ",result)
			print("==================")
		if(userChoice == 'Q'):
			print("Quitting....")
			break
	
if(__name__ == "__main__"):
    # Call main  
    main()
    
