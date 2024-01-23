# Contact Book 

'''
contact info fields : name, phone, email, address.

Contact Information : Store name, phone number, email, and address for each contact.
Add Contact         : Allow users to add new contacts with their details.
View Contact List   : Display a list of all saved contacts with names and phone numbers.
Search Contact      : Implement a search function to find contacts by name or phone number.
Update Contact      : Enable users to update contact details.
Delete Contact      : Provide an option to delete a contact.
User Interface      : Design a user-friendly interface for easy interaction.

'''

#====================================================================================================================#
                                            # Global Variables #
#====================================================================================================================#
# define list of dict that each dicts inside the list represent a contanct 
# dict key : name , phone, email, and address
# empty list and i will be on the following shape 
# [ {'name':'Ahmad', 'phone':'+201095932524','email':'ahmad.haroun2023@gmail.com','address':'Giza'},......]
contacts = []

#====================================================================================================================#
                                            # Functions Definition #
#====================================================================================================================#

# a function to add a new contact to the contact List 
def addContanct():
    name    = input("Enter Contact Name          : ")
    phone   = input("Enter Contact Phsone Number : ")
    email   = input("Enter Contact Email         : ")
    address = input("Enter Contact Address       : ")
    
    # add the info in the contacts List
    try:
        contacts.append({'name':name, 'phone': phone, 'email':email,'address':address})
        print("New Contact is added Successfully!")
    except Exception as e:
        print("!! new contact is not added!! ")
    print("=======================================")

# a function to view the list of contacts in the contact List
def viewContancts():
    if contacts:
        for contact in contacts:
            print(f"Name : {contact['name']}    Phone: {contact['phone']}")
    else:
        print("! List of Contacts is Empty !")
    print("=======================================")

# a function to seach for a contact in the existing List
def searchContanct():
    searchValue = input("Enter name or phone number: ")
    found = 0
    for contact in contacts:
        if( (searchValue == contact["name"])  or  (searchValue == contact["phone"]) ):
            print("Found!")
            # Ask the user if he/she wants to display the  info
            display = input("Do you want to display its info? Y/N ==>  ")
            if(display == 'Y'):
                print(f"Name  : {contact['name']}     Phone  : {contact['phone']}")
                print(f"email : {contact['email']}    address: {contact['address']}")
            found = 1
            break
    if(found == 0):
        print("!! Not Found !!")
    print("=======================================")
    return found

# a function to update the details or the info for the existing contact  
def updateContanct():
    # calling the searchContact Function to Take the name or phone to search for the required contact 
    # and return a result that indicated if the name is existed in the contact book or not 
    check =  searchContanct() 
    if(check == 1):
        print("1. Name")
        print("2. Phone")
        print("3. Email")
        print("4. Address")
        requiredInfo = input("Enter choice of Data you want to update: ")
        if(requiredInfo == '1'):   # Update Name 
            # Ask the user to enter the old name to be upadated 
            oldName  = input("Enter Old Name  : ")
            checkExisted = 0
            index = -1       # a variable to store the index of the oldName if Existed 
            # check if the oldName is correct 
            for contact in contacts:
                    index +=1
                    if(oldName == contact["name"]):
                        checkExisted = 1
                        break
           
            if(checkExisted == 1):
                newName1 = input("Enter new Name  : ")
                newName2 = input("Confirm new Name: ")
                if(newName1 == newName2):
                    contacts[index]["name"] = newName1
                    print("Name Updated Successfully!")
                else :
                    print("!! Confirmation Name Not Matched so Not Updated!! ")
            else:
                print("!! Old Name is not Correct !!")
        elif(requiredInfo == '2'): # Update phone 
            # Ask the user to enter the old phone number to be upadated 
            oldNumber  = input("Enter Old phone Number   : ")
            checkExisted = 0
            index = -1       # a variable to store the index of the oldNumber if Existed 
            # check if the oldNumber is correct 
            for contact in contacts:
                    index +=1
                    if(oldNumber == contact["phone"]):
                        checkExisted = 1
                        break
            if(checkExisted == 1):
                newNumber1 = input("Enter new phone Number   : ")
                newNumber2 = input("Confirm new phone Number : ")
                if(newNumber1 == newNumber2):
                    contacts[index]["phone"] = newNumber1
                    print("Phone Number Updated Successfully!")
                else :
                   print("!! Confirmation Phone Not Matched so Not Updated!!")
            else:
                print("!! Old phone number is not Correct !!")
        elif(requiredInfo == '3'): # Update email
            # Ask the user to enter the old Emaill Address to be upadated 
            oldEmail  = input("Enter Old Email    : ")
            checkExisted = 0
            index = -1         # a variable to store the index of the Email if Existed 
            # check if the Email is correct 
            for contact in contacts:
                    index +=1
                    if(oldEmail == contact["email"]):
                        checkExisted = 1
                        break
            if(checkExisted == 1):
                  newEmail1 = input("Enter new Email   : ")
                  newEmail2 = input("Confirm new Email : ")
                  if(newEmail1 == newEmail2):
                        contacts[index]["email"] = newEmail1
                        print("Email address Updated Successfully!")
                  else :
                    print("!! Confirmation Email Not Matched so Not Updated!!")
            else:
                print("!! old Email is not Correct !!")
        elif(requiredInfo == '4'): # Update address
            # Ask the user to enter the old Address to be upadated 
            oldAddress  = input("Enter old Address    : ")
            checkExisted = 0
            index = -1         # a variable to store the index of the Address if Existed 
            # check if the Address is correct 
            for contact in contacts:
                    index +=1
                    if(oldAddress == contact["address"]):
                        checkExisted = 1
                        break
            if(checkExisted == 1):
                  newAddress1 = input("Enter new Address   : ")
                  newAddress2 = input("Confirm new Address : ")
                  if(newAddress1 == newAddress2):
                        contacts[index]["address"] = newAddress1
                        print("Address Updated Successfully!")
                  else :
                    print("!! Confirmation Address Not Matched so Not Updated!!")
            else:
                print("!! old Address is not Correct !!")
        else:                      # invalid  input 
            print("!! Invalid Choice !!")
    else:
        print("!! Contact Not Found !!")        
    print("=======================================")

# a function to delete a contact from the contact List 
def deleteContanct():
    searchValue = input("Enter name or phone number: ")
    found = 0
    for contact in contacts:
        if( (searchValue == contact["name"]) or (searchValue == contact["phone"]) ):
            found = 1 # mark that the contact is Existed in the list 
            # Ask the user if he/she wants to display the  info before deleting 
            display = input("Do you want to display its info before deleting? Y/N ==>  ")
            if(display == 'Y'):
                print(f"Name  : {contact['name']}     Phone  : {contact['phone']}")
                print(f"email : {contact['email']}    address: {contact['address']}")
            lastCheck = input("Do you still want to remove ? Y/N ==> ")
            if(lastCheck == 'Y'):
                contacts.remove(contact)   # delete this contact from the list of contacts #
                print("The contact has been removed successfully!")
            break
    if(found == 0):
        print("!! Contact Not Found !!")
    print("=======================================")

# prompt the user to enter a choice 
def chooseOption():
    print("1. add    Contact")
    print("2. search Contact")
    print("3. update Contact")
    print("4. delete Contact")
    print("5. view   Contact")
    print("6. Quit"          )

    userChoice = input("Enter a choice : ")
    
    if( userChoice != '1' and userChoice != '2' and userChoice != '3' and 
        userChoice != '4' and userChoice != '5' and userChoice != '6'
      ):
        print("!! Invalide Input !!")
        print("=======================================")
        return "Invalid Input"
    else:
        return userChoice

# main code 
def main():

    '''
    1. add    Contact
    2. search Contact
    3. update Contact
    4. delete Contact
    5. view   Contacts
    6. Quit   

    '''
 
    while True:
        userChoice = chooseOption()
        if(userChoice == '1'):
            addContanct()
        if(userChoice == '2'):
            searchContanct()
        if(userChoice == '3'):
            updateContanct()
        if(userChoice == '4'):
            deleteContanct()
        if(userChoice == '5'):
            viewContancts()
        if(userChoice == '6'):
            print("Quitting....")
            break
        else: 
            # Do Nothing # 
            pass


# call the main function to start executing the program         
if (__name__ == "__main__"):
    main()