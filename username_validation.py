#This is a username validation program with the following rules:
#1. Username is no more than 12 characters.
#2. Username must not contain spaces.
#3. Username must not contain digits.

username = input("Enter your username:")
count=0
if len(username)<13:
    count += 1
else:
    print("The username can be no more than 12 characters.")

if username.find(" ")==-1:
    count += 1
else:
    print("The username can not contain spaces.")

if username.isalpha():
    count +=1
elif username.isalpha() == False and username.find(" ")>=0:
    print(" ")
else:
    print("The username can not contain digits.")

if count==3:
    print(f"Your username is valid!, Welcome {username}!")

input("Press any key to exit...")