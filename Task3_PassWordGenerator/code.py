#====================================================================================================================#
# Task:
# A password generator is a useful tool that generates strong and
# random passwords for users. This project aims to create a
# password generator application using Python, allowing users to
# specify the length and complexity of the password.

# User Input           : Prompt the user to specify the desired length of the
# password.

# Generate Password    : Use a combination of random characters to
# generate a password of the specified length.

# Display the Password : Print the generated password on the screen.
#====================================================================================================================#
import secrets
import string



#====================================================================================================================#
                                            # Functions Definition #
#====================================================================================================================#

# define a function to generate the password randomly 
def generate_random_password(length=12):
    
    # this is a string that contains all the alphapets (lower or upper case) + all digits(0-9)
    # and all the punctuation 
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # generate password randomly with secrets.choice(str) function and it 
    # choose the password by selecting the characters randomly from the str 
    password = ''.join(secrets.choice(characters) for i in range(length))
    
    # ==================================================== #
    # another syntax for the following line of code 
    # # Define an empty password Variable 
    # password = ''  
    # for i in range(length):
    #     password +=''.join(secrets.choice(characters))
     # ==================================================== #
    
    # return the generated password 
    return password

    
# main code
def main():
        passLength = (int)(input("Enter the length of the password : "))
        # Example: Generate a random password with default length (12 characters)
        passWord = generate_random_password(passLength)
        # display  the password 
        print("Generated Password: ",passWord)


# calling main 
if(__name__ == "__main__"):
    # Call main  
    main()



