#with open(r'udemy\day-25-start\weather_data.csv') as data_file:
#    data = data_file.readlines()
#print(data)

#import csv

#with open(r'udemy\day-25-start\weather_data.csv') as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] != 'temp':
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas as pd

path = r'udemy\day-25-start\weather_data.csv'
data = pd.read_csv(path)

#print(data['temp'])
#data_dict = data.to_dict()
#print(data_dict)

temperature_list = data['temp']

#average_temperature = sum(temperature_list)/len(temperature_list)
#print(temperature_list.mean())
#print(data.condition)

# Get Data in Row
#print(data[data.day == 'Monday'])

#print(data[data.temp == data.temp.max()])

#monday = data[data.day == 'Monday']
#monday_temp = monday.temp[0]
#monday_temp = monday_temp * 9/5 + 32

#print(monday_temp)

# Create Dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pd.DataFrame(data_dict)
new_data.to_csv('new_data.csv')