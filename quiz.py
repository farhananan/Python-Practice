def main():

    print("Hi there! Below is an 8 question quiz that will test your geography skills. Enjoy!")

    score = 0

    # Question 1
    answer = input("1. What is the capital city of New Zealand? ").lower()
    if answer == "wellington":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The answer is Wellington.")

    # Question 2
    answer = input("2. Which is the largest continent in the world? ").lower()
    if answer == "asia":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The answer is Asia.")

    # Question 3
    answer = input("3. What is the longest river in the world? ").lower()
    if answer == "nile":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The answer is the Nile River.")

    # Question 4
    answer = input("4. Which ocean is the largest? ").lower()
    if answer == "pacific ocean" or answer == "pacific":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The answer is the Pacific Ocean.")

    # Question 5
    answer = input("5. Mount Everest is located in which mountain range? ").lower()
    if answer == "himalayas" or answer == "himalaya":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The answer is the Himalayas.")

    # Question 6
    answer = input("6. Which country has the largest population in the world? ").lower()
    if answer == "india":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The answer is India.")

    # Question 7
    answer = input("7. What desert covers much of northern Africa? ").lower()
    if answer == "sahara" or answer == "sahara desert":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The answer is the Sahara Desert.")

    # Question 8
    answer = input("8. Which continent is Egypt located in? ").lower()
    if answer == "africa":
        print("Correct!")
        score += 1
    else:
        print("Incorrect! The answer is Africa.")

    # Final score
    print("\nQuiz Complete!")
    print("Your score:", score, "/ 8")

    if score == 8:
        print("Amazing! Perfect score!")
    elif score >= 6:
        print("Great job!")
        print("Try again and see if you can get a higher score!")
    elif score >= 4:
        print("Not bad!")
        print("Try again and see if you can get a higher score!")
    else:
        print("Keep practicing your geography!")
        print("Try again and see if you can get a higher score!")


# While loop to repeat the entire quiz
play_again = "yes"

while play_again == "yes":
    main()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()

print("Thanks for playing!")



