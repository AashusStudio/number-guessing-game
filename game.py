import random
import json
import os

DATA_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data.json"
)


# game function
def game(username, data):
    max_attempts = 7
    target_number = random.randint(1, 100)

    for attempt in range(1, max_attempts + 1):

        try:
            user_guess = int(input(f"\nAttempt {attempt}: "))
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            continue

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

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"user": {}}
    except json.JSONDecodeError:
        return {"user": {}}


# save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# login function
def login(data):

    while True:
        username_input = input("\nEnter your username: ")

        if username_input in data["user"]:
            password_input = input("\nEnter your pass: ")

            if password_input == data["user"][username_input]["pass"]:
                return username_input
            else:
                print("❗Password incorrect")

                retry = input("\nTry again? (y/n): ")
                if retry == "y":
                    continue
                elif retry == "n":
                    return None
                else:
                    print("\nInvalid input.\n")
                    return None
        else:
            print("❗Username not found\n")

        retry = input("Try again? (y/n): ")
        if retry == "y":
            continue
        elif retry == "n":
            return None
        else:
            print("Invalid input.\n")
            return None


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


def load_balance(data, username):
    return data["user"][username]["balance"]


while True:

    print("\n1. Login\n2. Sign up\n3. Leaderboard\n4. Exit\n")

    try:
        main_menu_choice = int(input(">> "))
    except ValueError:
            print("\nInvalid input. Please enter a valid number.")
            continue

    if main_menu_choice == 1:

        data = load_data()
        username = login(data)

        if username is not None:

            balance = load_balance(data, username)

            while True:
                print(f"\n=========[ 👤 {username} ]=========\n\n1. Balance\n2. Leaderboard\n3. Highlow guess (game)\n\n4. ← Back")

                try:
                    menu_choice = int(input("\n>> "))
                except ValueError:
                    print("Invalid input. input should be a number")
                    continue
                print("\n\n\n\n")
                if menu_choice == 1:
                    print(f"\nBALANCE -💲 {balance}")
                    

    elif main_menu_choice == 2:

        new_username = str(input("Create username: "))
        data = load_data()
        sign_in(new_username, data)

    elif main_menu_choice == 3:
        print("\nComing soon...")

    elif main_menu_choice == 4:
        print("\nThanks For Playing!")
        break

    else:
        print("\nInvalid")