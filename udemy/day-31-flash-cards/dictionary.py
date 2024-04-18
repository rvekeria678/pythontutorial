from config import DICTIONARY_PATH, TO_LEARN_PATH
import pandas
import json
import os

class Data:
    def __init__(self):
        self.data = {}
        self.to_learn = 0
        #if os.path.exists(TO_LEARN_PATH):
        #    self.data = pandas.read_csv(TO_LEARN_PATH).to_dict()
        #    self.to_learn = self.data['French'].keys()
        #else:
        #    with open(TO_LEARN_PATH, 'w') as data_file:
        #        self.data = pandas.read_csv(DICTIONARY_PATH)
        #        data_file.writelines(_ in range())
        data = pandas.read_csv(DICTIONARY_PATH)
    
    
        for index, row in data.iterrows():
            new_data = {
                row.French : row.English
            }
            try:
                with open(TO_LEARN_PATH, 'r') as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open(TO_LEARN_PATH,'w') as data_file:
                    json.dump(new_data, data_file, indent=3)
            else:
                with open(TO_LEARN_PATH, 'w') as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=3)

    def delete(self):
        pass

d = Data()


