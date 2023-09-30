from sys import exit
import json
import os
import copy
import time



user_name = ("jasen")
data_struct = {}
meals_per_day = input("Enter meals per day: ")
data_struct[user_name] = {}
data_struct[user_name]['meals'] = []
meal_num = []

valid_input_01 = False
meal_start = input("what time would you like to start this meal?")
if meal_start.isdigit() and float(meal_start)*2 >= 0 and float(meal_start)*2 <= 48:
    valid_input_01 = True
    meal_start = float(meal_start)*2
    print ("meal_start", meal_start)
else:
    print("Meal start time must fall on an hour or half-hour between 0 and 24, for example 8.5 is 8:30am. Please try again.")
    print()
