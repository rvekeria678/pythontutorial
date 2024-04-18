from config import DICTIONARY_PATH
import pandas

try:
    DATA = pandas.read_csv(DICTIONARY_PATH).to_dict()
except FileNotFoundError:
    print("Failed to load resources.")
