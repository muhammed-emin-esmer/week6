# Login system simulation

#Store the correct password (python123) in a variable.
#Create a Boolean variable logged_in and set it to False.
#Use a while loop to keep asking the user for a password while logged_in is False.
#If the password is correct, change logged_in to True and display "Login successful!".
# If the password is incorrect, display "Incorrect password. Try again." and ask again.


password = "python123"
logged_in = False
attempts = 0

while logged_in == False and attempts < 3:
    user_input = input("Enter the password: ")
    attempts = attempts + 1

    if user_input == password:
        print("Login successful!")
        logged_in = True
    else:
        print("Login failed. Try again.")

if logged_in == False:
        print("Too many failed attempts. Access denied.")


