#program name: login simulator program
#promgram Description: this program simulates a login system
#the user must enterthe correct password within three tries, or they'er locked out

#the correct password
password = "python"

#Variable to store user input
attempt = ""

# track the number of tries 
tries = 0

#loop conutiunes while the password is wrong and user hes tries left
while attempt != password and tries < 3:
    attempt = input("enter the password: ") # Ask user to type the password
    tries += 1 # and 1 to the sumber of tries

    #cheek if password is wrong 
    if attempt != password:
        print("incorrect password! try again. ")

# Ounce loop ends, cheek why it ended
if attempt == password:
    print("✅ Access granted!")
else:
    print("🚫 Too many attempts. Try later.") #If user ran out of tries