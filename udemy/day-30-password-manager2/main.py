from interface import PasswordManager
from password_generator import generate_password
import pyperclip
# ----- CONSTANTS ----- #
GENERATED_PASSWORD_LENGTH = 15
DATA_FILE_PATH = r'C:\Users\rveke\OneDrive\Documents\GitHub\pythontutorial\udemy\day-30-password-manager2\data.txt'
# ---- GENERATE PASSWORD ----- #
def fill_password():
    pm__ui.clear_password_input()
    new_password = generate_password(GENERATED_PASSWORD_LENGTH)
    pm__ui.fill_password_input(new_password)

# ----- SAVE PASSWORD ----- #
def save_password():
    website, user, password = pm__ui.website_input.get(), pm__ui.username_input.get(), pm__ui.password_input.get()

    if website and user and password:        
        if pm__ui.confirm_entry_message():
            with open(DATA_FILE_PATH, 'a') as data_file:
                data_file.write(f'{website} | {user} | {password}\n')
            # Clear Inputs
            pm__ui.clear_password_input()
            pm__ui.clear_website_input()
    else:
        pm__ui.missing_info_message()
# ----- UI SETUP ----- #
pm__ui = PasswordManager()

# ----- BIND OPERATIONS ----- #
pm__ui.add_button.config(command=save_password)
pm__ui.generate_button.config(command=generate_password)