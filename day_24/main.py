import pandas
# # getting data from columns
# weather_data = pandas.read_csv('./weather_data.csv')
# data_dict = weather_data.to_dict()
# temp_column = weather_data["temp"]
# temp_list = temp_column.to_list()

# print(temp_column.max(numeric_only=True))

# getting data from rows

# monday = weather_data.temp[weather_data.day == "Monday"]
# print(monday)
# fahreinheit = (monday * 9/5)+32
# print(fahreinheit)

s_data = pandas.read_csv('./squirel_data.csv')
fur_color_list =  s_data["Primary Fur Color"].to_list()
fur_dict = {"color":["Black","Gray","Cinnamon"],"total":[]}

black = fur_color_list.count("Black")
fur_dict["total"].append(black)
Gray = fur_color_list.count("Gray")
fur_dict["total"].append(Gray)
Cinnamon = fur_color_list.count("Cinnamon")
fur_dict["total"].append(Cinnamon)
data = pandas.DataFrame(fur_dict)
data.to_csv('total.csv')