import random
guess_number = random.randint(1,11)
user_guessing_number = input("Enter your guessing number")
count = 1
while(user_guessing_number.lower() != "exit"):
    if guess_number == int(user_guessing_number):
        print(f"Hurray!! You have guessed correctly in {count} times")
        break
    elif int(user_guessing_number) < guess_number:
        print(f" {user_guessing_number} is too low")
        count += 1
    else:
        print(f" {user_guessing_number} is too high")
        count += 1
    user_guessing_number = input("Enter your guessing number")
print("You successfully exit from the application")
