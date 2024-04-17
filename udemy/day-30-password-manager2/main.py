from interface import PasswordManager
from password_generator import generate_password
import pyperclip
# ----- CONSTANTS ----- #
GENERATED_PASSWORD_LENGTH = 15
DATA_FILE_PATH = r'C:\Users\rveke\OneDrive\Documents\GitHub\pythontutorial\udemy\day-30-password-manager2\data.txt'
# ---- GENERATE PASSWORD ----- #
def fill_password():
    pm.clear_password_input()
    new_password = generate_password(GENERATED_PASSWORD_LENGTH)
    pm.fill_password_input(new_password)
    pyperclip.copy(new_password)

# ----- SAVE PASSWORD ----- #
def save_password():
    website, user, password = pm.website_input.get(), pm.username_input.get(), pm.password_input.get()

    if website and user and password:        
        if pm.confirm_entry_message():
            try:
                with open(DATA_FILE_PATH, 'a') as data_file:
                    data_file.write(f'{website} | {user} | {password}\n')
            except FileNotFoundError:
                pm.missing_resources_message()
            else:
                # Clear Inputs
                pm.clear_password_input()
                pm.clear_website_input()
    else:
        pm.missing_info_message()
# ----- UI SETUP ----- #
pm = PasswordManager()

# ----- BIND OPERATIONS ----- #
pm.add_button.config(command=save_password)
pm.generate_button.config(command=fill_password)

pm.mainloop()