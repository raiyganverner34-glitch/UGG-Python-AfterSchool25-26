#program Description



name = input("enter your name: ")

#while loop will run as long as the variable name has nothing stored in it
while name == "" or not name.isalpha():
    print("you did not enter your name")
    #Asking the user to enter their name in case they didn't type anything
    name = input("enter your name: ")

    #exit out if the loop ouce the user has typed their 
    print(f"hello {name}")
