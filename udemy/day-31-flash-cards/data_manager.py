from config import DICTIONARY_PATH, TO_LEARN_PATH
import pandas, os, json, sys

class Data_Manager:
    def __init__(self):
        self.data = {}
        if not os.path.exists(TO_LEARN_PATH) or os.path.getsize(TO_LEARN_PATH) == 0:
            self.all_data()
        else:
            try:
                self.data = pandas.read_json(TO_LEARN_PATH).to_dict()
                if not self.data['French']:
                    self.clear_data()
                    self.all_data()
            except FileNotFoundError:
                print("Failed to load resources.")
                sys.exit(0)

    def clear_data(self):
        with open(TO_LEARN_PATH, 'w') as data_file:
            data_file.write('')

    def delete_data(self, index):
        if index in self.data['French'] and index in self.data['English']:
            self.data['French'].pop(index)
            self.data['English'].pop(index)
        else:
            print("Data has been corrupted. Closing application to reset save data.")
            self.clear_data()
            sys.exit(1)        
        self.save_data()

    def save_data(self):
        with open(TO_LEARN_PATH, 'w') as data_file:
            json.dump(self.data, data_file)

    def all_data(self):
        try:
            self.data = pandas.read_csv(DICTIONARY_PATH).to_dict()
        except FileNotFoundError:
            print("Failed to load resources.")
            sys.exit(0)
        finally:
            self.save_data()

    def data_size(self):
        return min(len(self.data['French']), len(self.data['English']))
    
    def data_keys(self):
        return list(self.data['French'].keys())