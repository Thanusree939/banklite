import os

# This file stores user data in the format: username,password,balance
USER_DATA_FILE = "users.txt"

# Load user data from the file into a dictionary
def load_users():
    users = {}
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            for line in f:
                username, password, balance = line.strip().split(",")
                users[username] = {"password": password, "balance": float(balance)}
    return users

# Save user data from the dictionary back to the file
def save_users(users):
    with open(USER_DATA_FILE, "w") as f:
        for username in users:
            data = users[username]
            f.write(f"{username},{data['password']},{data['balance']}\n")

# Register a new user
def register(users):
    print("\n--- Register ---")
    username = input("Enter a username: ")

    if username in users:
        print("❌ Username already exists. Try logging in.")
    else:
        password = input("Enter a password: ")
        users[username] = {"password": password, "balance": 0.0}
        print("✅ Registration successful!")

# Log in an existing user
def login(users):
    print("\n--- Login ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username]["password"] == password:
        print(f"✅ Welcome back, {username}!")
        banking_menu(username, users)
    else:
        print("❌ Invalid username or password.")

# Menu after logging in
def banking_menu(username, users):
    while True:
        print(f"\n--- {username}'s Account ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"💰 Your balance is: ₹{users[username]['balance']}")
        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            users[username]['balance'] += amount
            print("✅ Deposit successful.")
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= users[username]['balance']:
                users[username]['balance'] -= amount
                print("✅ Withdrawal successful.")
            else:
                print("❌ Insufficient balance.")
        elif choice == "4":
            print("👋 Logged out.")
            break
        else:
            print("Invalid option.")

# Main menu for the app
def main():
    users = load_users()  # Load existing users from file
    print("===== Welcome to BankLite =====")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register(users)
        elif choice == "2":
            login(users)
        elif choice == "3":
            save_users(users)
            print("Thank you for using BankLite!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the program
if __name__ == "__main__":
    main()
