# Create a student email creator that uses first and last name plus id
# eg. smithjohn123@fake.school.nz

# Get input (first, last, id) and save in variables
print ("Welcome to the student email creator! Please enter your first name:")
first_name = input()
print ("Please enter your last name:")
last_name = input()
print ("Please enter your ID:")
id = input()

# Strip input to remove accidental spaces and turn names into lowercase (resave in variables)
first_name = first_name.strip().lower()
last_name = last_name.strip().lower()
id = id.strip()



# Output the final email address
print("Your student email is:", last_name + first_name + id + "@wsc.school.nz")


# --------------------------------

# EXTENSION
# Create a temporary password to output as well
print("Your temporary password is:", first_name.upper() + str(int(id) // 10) + last_name.upper())
# It should be their names in all uppercase and their id divided by 10

# --------------------------------

# EXPERT
# Create a WSCW email creator
# Get the users first and last name, then randomly generate an ID number (8 digits long)
# Output the email addess (lastf.wsc.school.nz) 
# - you'll need to strip down the first name to just first letter
# Output their id number
# Output a temporary password (all uppercase). You can choose how you create this, 
# but it needs to be unique for each user