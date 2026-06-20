import random
import json


# game function
def game(username, data):
    max_attempts = 7
    target_number = random.randint(1, 100)

    for attempt in range(1, max_attempts + 1):

        user_guess = int(input(f"\nAttempt {attempt}: "))

        if target_number == user_guess:
            reward_points = int(100 / attempt)
            data["user"][username]["balance"] += reward_points
            save_data(data)

            print(f"\nCorrect! in {attempt} attempt, Rewarded {reward_points} Points\n")
            break

        else:
            if attempt < max_attempts:
                if target_number > user_guess:
                    print("\nTry Higher! 📈")
                else:
                    print("\nTry Lower! 📉")
            else:
                print(f"Better Luck Next Time, The Number Was {target_number}\n")


# load data
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)


# save data
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


# login function
def login(data):

    username_input = str(input("Enter your username: "))

    if username_input in data["user"]:
        password_input = str(input("Enter your pass: "))

        if password_input == data["user"][username_input]["pass"]:
            return username_input
        else:
            print("❗password not match\n")

    else:
        print("❗username not match\n")


# sign in function
def sign_in(new_username, data):

    if new_username in data["user"]:
        print(f"The username {new_username} is already taken")

    elif new_username != "":
        new_password = str(input("Create a password: "))

        if new_password != "":
            data["user"][new_username] = {
                "pass": new_password,
                "balance": 0
            }
            save_data(data)
        else:
            print("Invalid password")

    else:
        print("Invalid username")


while True:

    print("\n1. Login\n2. Sign up\n3. Leaderboard\n")

    menu_choice = int(input(">> "))

    if menu_choice == 1:

        data = load_data()
        username = login(data)

        if username is not None:
            game(username, data)

            while True:

                print("Want to play again ? (y/n)")
                replay_choice = str(input(">>(y/n): "))

                if replay_choice == "y":
                    game(username, data)

                elif replay_choice == "n":
                    print("\nThanks For Playing!")
                    break

    elif menu_choice == 2:

        new_username = str(input("Create username: "))
        data = load_data()
        sign_in(new_username, data)

    elif menu_choice == 3:
        print("\nComing soon...")

    else:
        print("\nInvalid")