import getpass
import string
import os
import rsa

#public key to encrypt the password
#private key to decrypt the password

# Read the RSA key from a text file, catch the error if the file is not found
try:
    with open ('keys/privkey.pem', 'rb') as f:
        #first encode the key to bytes, then load it
        privkeyplaintext = f.read().decode()
        privkey = rsa.PrivateKey.load_pkcs1(privkeyplaintext)
    with open ('keys/pubkey.pem', 'rb') as m:
        pubkeyplaintext = m.read().decode()
        pubkey = rsa.PublicKey.load_pkcs1(pubkeyplaintext)

except FileNotFoundError:
    print("RSA keys not found. They should be in the 'keys' folder.")
    print("Enter 1 to generate new keys, or 2 to exit.")
    choice = input("Choice: ")
    if choice == '1':
        #generate the keys
        pubkey, privkey = rsa.newkeys(512)

        #write the keys to the file
        with open ('keys/privkey.pem', 'wb') as f:
            f.write(privkey.save_pkcs1('PEM'))
        with open ('keys/pubkey.pem', 'wb') as f:
            f.write(pubkey.save_pkcs1('PEM'))

        print("RSA keys generated and saved in the 'keys' folder.")
        print("Deleting current logins.txt file, as the keys have changed.")
        try:
            os.remove('logins.txt')
            print("logins.txt file deleted.")
        except FileNotFoundError:
            print("No logins.txt file found, one will get generated at the next step.")
    else:
        exit()

#import a "datasheet" dictionary variable from logins.txt, or create a new one if the file is not found
try:
    with open('logins.txt', 'rb') as f:
        datasheet = eval(f.read())
        print("Logins.txt file loaded!.")
except FileNotFoundError:
    datasheet = {}
    print("No logins.txt file found. Creating a new one.")


def add_password(account, password):
    account = string.capwords(account)
    if account in datasheet:
        print(f"Account '{account}' already exists.")
        return
    #encrypt the password
    password = rsa.encrypt(password.encode(), pubkey)
    #write the encrypted password to the file
    with open('logins.txt', 'wb') as f:
        f.write(str(datasheet).encode())


def get_password(account):
    account = string.capwords(account)
    if account in datasheet:
        return rsa.decrypt(datasheet[account], privkey).decode()
    else:
        return False

def list_accounts():
    if not datasheet:
        print("Password manager is currently empty.")
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
