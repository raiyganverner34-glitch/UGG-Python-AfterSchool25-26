#countdown timer program
#promgram Descriptions: this program count down time from a user-given number 10 1.

#importting time to add 1 secound delay
import time 

#Ask the user to enter a number to start counting down from
number = int(input("enter a number to start the countdown: "))

#keep looping as long as the number id greater than 0
while number > 0:
    print(number)
    time.sleep(1)
    number -= 1

    #ounce the loop ends print a message
    print("🎉 time ")