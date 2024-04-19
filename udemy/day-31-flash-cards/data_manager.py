from config import DICTIONARY_PATH, TO_LEARN_PATH
import pandas, os, json, sys

class Data_Manager:
    def __init__(self):
        self.data = {}
        if not os.path.exists(TO_LEARN_PATH) or os.path.getsize(TO_LEARN_PATH) == 0:
            self.all_data()
        else:
            try:
                self.data = pandas.read_json(TO_LEARN_PATH).to_json()
            except:
                print("Failed to load resources.")
                sys.exit(0)

    def delete_data(self, index):
        pass

    def save_data(self, index):
        with open(TO_LEARN_PATH, 'w') as data_file:
            json.dump(self.data, data_file)

    def all_data(self):
        try:
            self.data = pandas.read_csv(DICTIONARY_PATH).to_json()
        except FileNotFoundError:
            print("Failed to load resources.")
            sys.exit(0)
        finally:
            self.save_data()

data_manager = Data_Manager()


