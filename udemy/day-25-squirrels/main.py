import pandas as pd

path = r'udemy\day-25-squirrels\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240415.csv'

data = pd.read_csv(path)
grey_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])


#print(grey_squirrels_count)
#print(cinnamon_squirrels_count)
#print(black_squirrels_count)

data_dict = {
    'Fur Color': ["Gray", 'Cinnamon', 'Black'],
    'Count': [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pd.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')