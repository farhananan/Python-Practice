# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input
print ("Welcome to the roller coaster access screener! Please enter your height in cm:")
height = int(input())
print ("please enter your age:")
age = int(input())
if age > 10 and height > 150:
    print ("Do you have a heart condition? (y/n)")
    if input() == "y":
        print("Sorry, you cannot ride.")
    else:
           print ("Do you have a VIP pass? (y/n)")
    if input() == "y":
            print("Access granted! Enjoy the ride!")
            





# Check conditions and output verdict





# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient