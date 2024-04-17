from interface import PasswordManager
from password_generator import generate_password
import pyperclip
import json
# ----- CONSTANTS ----- #
GENERATED_PASSWORD_LENGTH = 15
DATA_FILE_PATH = r'C:\Users\rveke\OneDrive\Documents\GitHub\pythontutorial\udemy\day-30-password-manager2\data.json'
# ---- GENERATE PASSWORD ----- #
def fill_password():
    pm.clear_password_input()
    new_password = generate_password(GENERATED_PASSWORD_LENGTH)
    pm.fill_password_input(new_password)
    pyperclip.copy(new_password)

# ----- SAVE PASSWORD ----- #
def save_password():
    website, user, password = pm.website_input.get(), pm.username_input.get(), pm.password_input.get()
    new_data = {website:{
            "email" : user,
            "password" : password
        }
    }

    if website and user and password:        
        if pm.confirm_entry_message():
            try:
                with open(DATA_FILE_PATH, 'r') as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open(DATA_FILE_PATH,'w') as data_file:
                    json.dump(new_data, data_file, indent=3)
            else:
                with open(DATA_FILE_PATH, 'w') as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=3)
            finally:
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