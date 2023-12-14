import os
import rsa
import base64
import hashlib
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

# Main application window
root = tk.Tk()
root.title("Secure Registration and Login System")

# Notebook for tabs
tab_control = ttk.Notebook(root)

# Registration tab
reg_tab = ttk.Frame(tab_control)
tab_control.add(reg_tab, text='Register')

# Login tab
login_tab = ttk.Frame(tab_control)
tab_control.add(login_tab, text='Login')

tab_control.pack(expand=1, fill="both")

# Registration widgets
reg_username_label = tk.Label(reg_tab, text="Username")
reg_username_label.pack()
reg_username_entry = tk.Entry(reg_tab)
reg_username_entry.pack()

reg_password_label = tk.Label(reg_tab, text="Password")
reg_password_label.pack()
reg_password_entry = tk.Entry(reg_tab, show="*")
reg_password_entry.pack()

reg_submit_button = tk.Button(reg_tab, text="Register")
reg_submit_button.pack()

# Login widgets
login_username_label = tk.Label(login_tab, text="Username")
login_username_label.pack()
login_username_entry = tk.Entry(login_tab)
login_username_entry.pack()

login_password_label = tk.Label(login_tab, text="Password")
login_password_label.pack()
login_password_entry = tk.Entry(login_tab, show="*")
login_password_entry.pack()

login_submit_button = tk.Button(login_tab, text="Login")
login_submit_button.pack()

# RSA key generation
global public_key, private_key


def get_rsa_keys():
    global public_key, private_key
    KEY_SIZE = 2048

    def generate_keys():
        global public_key, private_key
        print("Generating RSA keys...")
        public_key, private_key = rsa.newkeys(KEY_SIZE)
        with open('public_key.pem', mode='wb') as public_file:
            public_file.write(public_key.save_pkcs1())
        with open('private_key.pem', mode='wb') as private_file:
            private_file.write(private_key.save_pkcs1())
        print("Keys generated!")

    if os.path.exists('public_key.pem') and os.path.exists('private_key.pem'):
        try:
            with open('public_key.pem', mode='rb') as public_file:
                public_key = rsa.PublicKey.load_pkcs1(public_file.read())
            with open('private_key.pem', mode='rb') as private_file:
                private_key = rsa.PrivateKey.load_pkcs1(private_file.read())
            print("Keys loaded successfully!")
        except:
            generate_keys()
    else:
        generate_keys()

    return public_key, private_key


def display_user_list(usernames, remove_user_callback):
    # Create a new window
    list_window = tk.Toplevel()
    list_window.title("User List")

    # Create a listbox widget
    listbox = tk.Listbox(list_window, selectmode=tk.SINGLE)
    listbox.pack(fill=tk.BOTH, expand=True)

    # Insert usernames into the listbox
    for username in usernames:
        listbox.insert(tk.END, username)

    # Add a scrollbar
    scrollbar = ttk.Scrollbar(list_window, orient='vertical', command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    listbox.config(yscrollcommand=scrollbar.set)

    # Remove Button
    remove_button = tk.Button(list_window, text="Remove", command=lambda: remove_user_callback(listbox))
    remove_button.pack()

    # Run the window's main loop
    list_window.mainloop()


def remove_user(listbox):
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)


# Backend Functions
def register_user():
    global public_key, private_key
    username = reg_username_entry.get()
    password = reg_password_entry.get()

    if not username or not password:
        tk.messagebox.showerror(title="Error", message="Please enter both username and password.")
        return

    # Hash the password using sha256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Check if the username already exists
    if check_username_exists(username):
        tk.messagebox.showerror(title="Error", message="Username already exists. Please choose a different one.")
        return

    # Save the username and hashed password to the file
    if save_to_file(username, hashed_password):
        tk.messagebox.showinfo(title="Success", message="Account registered successfully!")
    else:
        tk.messagebox.showerror(title="Error", message="Failed to register account.")


def login_user():
    global public_key, private_key
    username = login_username_entry.get()
    password = login_password_entry.get()

    if not username or not password:
        tk.messagebox.showerror(title="Error", message="Please enter both username and password.")
        return

    # Hash the password using sha256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Validate the login
    if validate_account(username, hashed_password):
        tk.messagebox.showinfo(title="Success", message="Login successful!")
        # Get the list of usernames and display them in a new window
        display_user_list(get_user_list(), remove_user)
    else:
        tk.messagebox.showerror(title="Error", message="Incorrect username or password.")


def save_to_file(username, password_hash):
    global public_key, private_key

    # Encrypt the username and password with RSA
    encrypted_username = rsa.encrypt(username.encode(), public_key)
    encrypted_password = rsa.encrypt(password_hash.encode(), public_key)

    # Encode the encrypted data as base64
    encoded_username = base64.b64encode(encrypted_username).decode()
    encoded_password = base64.b64encode(encrypted_password).decode()

    # Save credentials to 'accounts.txt'
    with open('accounts.txt', mode='a') as file:
        file.write(f"{encoded_username}\t{encoded_password}\n")

    return True


def check_username_exists(username):
    global public_key, private_key
    if os.path.exists('accounts.txt'):
        with open('accounts.txt', mode='r') as file:
            for line in file:
                encrypted_username, _ = line.strip().split('\t')
                decrypted_username = rsa.decrypt(base64.b64decode(encrypted_username), private_key).decode()
                if decrypted_username == username:
                    return True
    return False


def validate_account(username, attempted_hash):
    global public_key, private_key
    if os.path.exists('accounts.txt'):
        with open('accounts.txt', mode='r') as file:
            for line in file:
                encrypted_username, encrypted_password = line.strip().split('\t')
                decrypted_username = rsa.decrypt(base64.b64decode(encrypted_username), private_key).decode()
                decrypted_password = rsa.decrypt(base64.b64decode(encrypted_password), private_key).decode()
                if decrypted_username == username and decrypted_password == attempted_hash:
                    return True
    return False


def get_user_list():
    global public_key, private_key
    usernames = []
    if os.path.exists('accounts.txt'):
        with open('accounts.txt', mode='r') as file:
            for line in file:
                encrypted_username, _ = line.strip().split('\t')
                decrypted_username = rsa.decrypt(base64.b64decode(encrypted_username), private_key).decode()
                usernames.append(decrypted_username)
    return usernames


# Bind functions to buttons
reg_submit_button.config(command=register_user)
login_submit_button.config(command=login_user)

# Main loop to run the application
get_rsa_keys()
root.mainloop()