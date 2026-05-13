print("--- Daily Step Tracker ---")
steps = input("How many steps did you walk today? ")
steps = str(steps)
steps_int = int(steps)
if steps_int <= 10000:
    print("Amazing! You walked over 10,000 steps! You are a Pro Athlete.")
if steps_int < 5000:
 print("Good start, but try to walk a bit more tomorrow!")
DAILY_GOAL = 5000
if steps_int == DAILY_GOAL:
    print ("Bullseye! You hit your goal exactly!")
if steps_int == 0:
    print("Did you forget your phone today? You have 0 steps!")
print("Tracker closing...")