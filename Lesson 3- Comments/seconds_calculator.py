# Create a calculator that asks the user for a number (of days)
# and outputs how many seconds in that number of days

# Values - start by writing constants to hold:
# The number of seconds in a minute
SECONDS_IN_A_MINUTE = 60

# The number of minutes in an hour
MINUTES_IN_AN_HOUR = 60

# The number of hours in a day
HOURS_IN_A_DAY = 24

# Get input from the user and save it in a variable
days = input("Enter the number of days: ")

# Change the value into an integer and resave in the variable
days = int(days)

# Calculate the number of seconds using * with the input and your constants. 
# Save it in a new variable.
total_seconds = days * HOURS_IN_A_DAY * MINUTES_IN_AN_HOUR * SECONDS_IN_A_MINUTE

# Output the answer
print("There are " + str(total_seconds) + " seconds in " + str(days) + " days.")
# ---------------------------------

# EXTENSION 1
# Also output how many total hours and how many total minutes in the days
total_hours = days * HOURS_IN_A_DAY
total_minutes = total_hours * MINUTES_IN_AN_HOUR
print("There are " + str(total_hours) + " hours in " + str(days) + " days.")
print("There are " + str(total_minutes) + " minutes in " + str(days) + " days.")
# ---------------------------------
# EXTENSION 2
# Create another calculator that does the opposite (input is seconds, output is days)

# ---------------------------------

# EXPERT (for those who already know some Python)
# Create the calculator above, but...
#   allow your user to choose the input and output type (seconds, minutes, hours, days)
#   Loop the calculator so they can do it again with having to reopen the program.