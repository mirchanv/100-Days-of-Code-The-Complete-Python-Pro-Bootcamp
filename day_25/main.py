import csv
import pandas

# option 1:
with open("weather_data.csv") as file:
    data = file.readlines()
    print(data)

# option 2 - using csv module (better tan option1):
with open("weather_data.csv", mode="r") as data_file:
    csv_file = csv.reader(data_file)
    temperatures = []
    for data_row in csv_file:
        print(data_row)
        if data_row[1] != "temp":
            temperatures.append(int(data_row[1]))
    print(temperatures)

# option 3 - using pandas module (recommended way)
csv_data = pandas.read_csv("weather_data.csv")
print(csv_data)

# selecting a column
print(csv_data["temp"])

# converting the whole data frame to a dict
# each column is a separate dict
data_dict = csv_data.to_dict()
print(data_dict)
print(data_dict["day"])
print(data_dict["temp"])
print(data_dict["condition"])

# converting Series to List
list_of_temps = csv_data["temp"].to_list()
print(type(list_of_temps), list_of_temps)

sum_temps = 0
for temp in list_of_temps:
    sum_temps += temp

avg_temp = sum(list_of_temps) / len(list_of_temps)
print("Avg Temp = ", "{:0.2f}".format(round(avg_temp, 2)))

total_temp = csv_data["temp"].mean()
print("Avg Temp = ", "{:0.2f}".format(round(total_temp, 2)))

max_temp = csv_data["temp"].max()
print("Max Temp = ", max_temp)

# getting a specific row
monday_row = csv_data[csv_data.day == "Monday"]
print(monday_row)

# getting the row with max temp
print(csv_data[csv_data.temp == csv_data.temp.max()])

monday_temp_C = monday_row.temp[0]
monday_temp_F = (monday_temp_C * 1.8) + 32
print(monday_temp_F)

# creating a DataFrame from scratch
friends_info = {
    "friends": ["Rocky", "Tommy", "Harry"],
    "ages": [25, 35, 45]
}

content = {"Name": friends_info["friends"], "Age": friends_info["ages"]}
data_frame = pandas.DataFrame(data=content)
print(data_frame)

# we can also directly do
data_frame = pandas.DataFrame(friends_info)
print(data_frame)

# saving data to csv file
data_frame.to_csv("friends_data.csv")