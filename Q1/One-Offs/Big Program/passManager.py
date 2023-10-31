import getpass
import string
import os
import rsa

# Read the RSA key from a text file, catch the error if the file is not found
with open("key.txt", "r") as key_file:
    rsa_key = key_file.read()
    try:
        rsa_key = rsa.PrivateKey.load_pkcs1(rsa_key)
        print("RSA key loaded successfully.")
        print("Your RSA key is: ", str(rsa_key))
    except:
        print("Unable to load RSA key. Check for the key.txt file in the same directory as this program.")
        exit()


# Initialize an empty list to store account-password pairs
datasheet = {}

def add_password(account, password):
    account = string.capwords(account)
    if account in datasheet:
        print(f"Account '{account}' already exists.")
        return
    datasheet[account] = password

def get_password(account):
    account = string.capwords(account)
    if account in datasheet:
        return datasheet[account]
    else:
        return False

def list_accounts():
    if not datasheet:
        print("Password manager is empty.")
        return

    print("Stored accounts:")
    for account in datasheet:
        print(account)

while True:
    print("----------------------------")
    print("\nPassword Manager Menu:")
    print("1. Add an account")
    print("2. Get a password")
    print("3. List accounts")
    print("4. Quit")
    print("----------------------------")
    print('\n')

    choice = input("Select an option (1/2/3/4): ")

    if choice == '1':
        #clear screen and write header
        os.system('cls')

        print("----------------------------")
        print("Registering an Account")
        print("----------------------------\n\n")

        account = input("Enter account name: ")
        password = input("Enter the password: ")
        add_password(account, password)

    elif choice == '2':
        # clear screen and write header
        os.system('cls')

        print("----------------------------")
        print("Getting a password")
        print("----------------------------\n\n")

        account = string.capwords(input("Enter account name: "))
        password = get_password(account)
        if password:
            print(f"Password for '{account}': {password}")
        else:
            print(f"Account '{account}' not found.")
    elif choice == '3':
        # clear screen and write header
        os.system('cls')

        print("----------------------------")
        print("Account List")
        print("----------------------------\n\n")

        list_accounts()
    elif choice == '4':
        break
    else:
        print("Invalid option. Please select a valid option (1/2/3/4).")

print("Thank you for using the Password Manager.")
