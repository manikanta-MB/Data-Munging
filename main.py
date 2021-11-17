"""This Program Extracts Weather and Soccer game data and then displays
day number with smallest temperature spread and team name with smallest
difference between A and F columns.
The Main purpose of this program is using of SOLID Principles of OOPS.
"""

import os

CURRENT_WORKING_DIRECTORY = os.getcwd()

class DataExtractor:
    """This class extracts the data of certain columns from the given file"""
    def __init__(self,data_location):
        self.data_location = data_location
    # fetching required column values from a particular row
    def fetch_column_values(self,line,col_indexes):
        # This statement deletes extra spaces between columns
        columns = filter(lambda word:word.strip(),line.split(' '))
        col_values = []
        for col_index in col_indexes:
            col_values.append(columns[col_index])
        return col_values
    # fetching required column values from all rows
    def get_column_values(self,*col_indexes):
        with open(self.data_location,"r") as f:
            f.readline() # skipping the headers
            all_row_column_values = []
            for line in f:
                col_values = self.fetch_column_values(line,col_indexes)
                all_row_column_values.append(col_values)
            return all_row_column_values

class DataAnalyzer:
    """This Class analyzes the data based on given conditions."""
    def __init__(self):
        pass
    # It finds the label name with smallest difference between given columns
    def get_min_difference(self,data):
        min_diff = float("inf")
        min_label = None
        for label,val1,val2 in data:
            current_diff = abs(float(val1)-float(val2))
            if(current_diff < min_diff):
                min_diff = current_diff
                min_label = label
        return min_label

class Weather:
    """This Class Analyzes the Weather Data"""
    def __init__(self,data_location,day_number_index,max_temp_index,min_temp_index):
        self.data_extractor = DataExtractor(data_location)
        self.data_analyzer = DataAnalyzer()
        self.day_number_index = day_number_index
        self.max_temperature_index = max_temp_index
        self.min_temperature_index = min_temp_index
    # It calculates the day number with smallest temperature spread
    def get_day_number_with_smallest_temperature_spread(self):
        every_day_temperatures = self.data_extractor.get_column_values(
            self.day_number_index,self.max_temperature_index,self.min_temperature_index
            )
        day_number = self.data_analyzer.get_min_difference(every_day_temperatures)
        return day_number

class Soccer:
    """This Class Analyzes the Soccer Game Data"""
    def __init__(self,data_location,team_name_index,f_column_index,a_column_index):
        self.data_extractor = DataExtractor(data_location)
        self.data_analyzer = DataAnalyzer()
        self.team_name_index = team_name_index
        self.f_index = f_column_index
        self.a_index = a_column_index
    # It calculates the team name with smallest difference between A and F columns
    def get_team_name_with_smallest_diff_between_a_and_f(self):
        every_team_a_and_f = self.data_extractor.get_column_values(
            self.team_name_index,self.f_index,self.a_index
            )
        team_name = self.data_analyzer.get_min_difference(every_team_a_and_f)
        return team_name

weather = Weather(CURRENT_WORKING_DIRECTORY+"/Data/weather.dat",0,1,2)
soccer = Soccer(CURRENT_WORKING_DIRECTORY+"/Data/football.dat",1,6,7)

day_number = weather.get_day_number_with_smallest_temperature_spread()
print("Day Number with smallest temperature spread is {}".format(day_number))

team_name = soccer.get_team_name_with_smallest_diff_between_a_and_f()
print("Team Name with smallest difference between A and F is {}".format(team_name))
