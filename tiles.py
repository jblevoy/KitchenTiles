from sys import exit
import json
import os
import copy
import time


def menu():
    os.system('clear')
    print('╔'+ '═'*120+ '╗')
    print("\t\tWelcome to KitchenTiles™, the new way to reduce passive-aggressive kitchen-based inconveniences")
    print()
    print("Enter the number of your choice:")
    print("\t1. Enter a new user")
    print("\t2. Update a mealtime")
    print("\t3. Add a meal")
    print("\t4. Remove a meal")
    print("\t5. Remove a user")
    print("\t6. Display Kitchen Day Planner")
    print("\t7. Save to file")
    print("\t8. Restore from file")
    print("\t9. Exit")
    print()
    choice = input("  > ")
    return choice

def print_data(data_struct):
    data_struct_copy = copy.deepcopy(data_struct)
    print_string = ""
    print('╔'+ '═'*120+ '╗')
    print("\t\t\t\tDay Viewer Mode 12 AM to 12 PM\t\t\t\t\t(User)")
    print()
    for user_name in data_struct_copy.keys():

        meals = data_struct_copy[user_name]['meals']
        if len(meals) == 0:
            print_string = (" "*96)
        else:    
            meal = meals.pop(0)
            for half_hour in range(48):
                to_add = ""
                start_meal,end_meal = meal

                if half_hour < start_meal:
                    to_add = "  "
                if half_hour >= start_meal:
                    to_add = "██"
                if half_hour >= end_meal:
                    to_add = "  "
                    if len(meals) > 0:
                        meal = meals.pop(0)

                print_string += to_add
        print_string += user_name + '\n'
    print(print_string)
    print('╚'+ '═'*120+ '╝')
    done = input("Press 'Enter' when done.")
    return data_struct


def create_user(data_struct):
    user_name = input("Enter User Name: ")
    meals_per_day = input("Enter meals per day: ")
    data_struct[user_name] = {}
    data_struct[user_name]['meals'] = []
    meal_num = []
    for k in range(int(meals_per_day), 0, -1):
        if k == 1:
            meal_num.append('first')
        if k == 2:
            meal_num.append('second')
        if k == 3:
            meal_num.append('third')
        if k == 4:
            meal_num.append('forth')
        if k == 5:
            meal_num.append('fifth')
        if k == 6:
            meal_num.append('sixth')
        if k == 7:
            meal_num.append('seventh')

    for j in range(int(meals_per_day)):
        valid_input_01 = False
        while valid_input_01 == False:
            meal_start = input("Enter start time of {} meal: ".format(meal_num[(int(meals_per_day)-1)-j]))
            try:
                float(meal_start)
                try:
                    float(meal_start)*2 >= 0 and float(meal_start)*2 <= 48
                    valid_input_01 = True
                    meal_start = float(meal_start)*2
                    print ("meal start time ", meal_start/2)
                except:
                    pass
            except:
                print("Meal start time must fall on an hour or half-hour between 0 and 24, for example 8.5 is 8:30am. Please try again.")
                print()
                pass

        valid_input_02 = False
        while valid_input_02 == False:
            meal_end = input("Enter end time of {} meal: ".format(meal_num[(int(meals_per_day)-1)-j]))
            try:
                float(meal_end)
                if float(meal_end)*2 >= 0 and float(meal_end)*2 <= 48:
                    valid_input_02 = True
                    meal_end=float(meal_end)*2
                    print("meal end time ", meal_end/2)
                else:
                    print("Meal end time must be after start, and fall on an hour or half-hour between 0 and 24, for example 8.5 is 8:30am. Please try again.")
                    print()
            except:
                print("Meal end time must be after start, and fall on an hour or half-hour between 0 and 24, for example 8.5 is 8:30am. Please try again.")
                print()
                pass
        data_struct[user_name]['meals'].append((meal_start, meal_end))
        data_struct[user_name]['meals'].sort()


        for i in range(len(data_struct[user_name]['meals'])):
            if data_struct[user_name]['meals'][i] == (meal_start,meal_end):
                index_of_input = i
        if index_of_input == 0:
            a = 0
            b = 0
            index_tuple = data_struct[user_name]['meals'][index_of_input]
            c,d = index_tuple
        else:
            pre_index_tuple = data_struct[user_name]['meals'][index_of_input - 1]
            a,b = pre_index_tuple
            index_tuple = data_struct[user_name]['meals'][index_of_input]
            c,d = index_tuple
        try:
            post_index_tuple = data_struct[user_name]['meals'][index_of_input + 1]
            e,f = post_index_tuple
        except:
            e = meal_end + 1
            f = e
        if c < b or d > e:
            del data_struct[user_name]['meals'][index_of_input]
            print("This meal cannot be added because it conflicts with another mealtime.")
    ok = input("All valid meals added. Now returning to main menu, press enter to proceed.") 
    
    return data_struct



def remove_user(data_struct):
    print('═'*120)
    print("\t\t\tRemove User")
    print()
    if len(data_struct) > 0:
        while True:
            which_user = input("Which user would you like to remove? ")
            if which_user in data_struct:
                del data_struct[which_user]
                break
            else:                
                print("That user is not yet registered, please try again.")
                print()
        ok = input("{} has been removed from the kitchen. Now returning to main menu, press enter to proceed.".format(which_user))
    else:
        ok = input("No users to remove! Now returning to main menu, press enter to proceed.")

def remove_meal(data_struct):
    which_meal=['\t1. First', '\t2. Second', '\t3. Third', '\t4. Fourth']
    print('═'*120)
    print("\t\t\tRemove Meal")
    print()
    if len(data_struct) > 0:
        while True:
            which_user = input("For which user would you like to remove a meal? ")
            if which_user in data_struct:
                break
            else:
                print("That user is not yet registered, please try again.")
                print()
        print()
        if len(data_struct[which_user]['meals']) > 0:
            for x in range(len(data_struct[which_user]['meals'])):
                meal = data_struct[which_user]['meals'][x]
                start_meal,end_meal = meal
                print(which_meal[x], "Start: ", start_meal / 2, "End: ", end_meal /2)

            print()
            valid_input_03 = False
            while valid_input_03 == False:
                meal_index = input("Which meal would you like to remove? ")
                if meal_index.isdigit() and int(meal_index) >= 1 and int(meal_index) <= len(data_struct[which_user]['meals']):
                    valid_input_03 = True
                else:
                    print("Please enter a number corresponding to the meal you would like to remove")
                    print()
            meal_index = int(meal_index) - 1
            del data_struct[which_user]['meals'][meal_index]
            ok = input("Meal has been removed. Now returning to main menu, press enter to proceed.")
        else:
            ok = input("No meals to remove! To add a meal, select option 3 from main menu. Now returning to menu, press enter to proceed.")
    else:
        ok = input("No users, no meals to remove! Now returning to main menu, press enter to proceed.")

def add_meal(data_struct):
    while True:
        user_name = input("For which user would you like to add a meal? ")
        if user_name in data_struct:
            break
        else:
            print("That user is not yet registered, please try again")
    
    valid_input_01 = False
    while valid_input_01 == False:
        meal_start = input("When will this meal start? ")
        try:
            float(meal_start)
            try:
                float(meal_start)*2 >= 0 and float(meal_start)*2 <= 48
                valid_input_01 = True
                meal_start = float(meal_start)*2
                print ("meal start time ", meal_start/2)
            except:
                pass
        except:
            print("Meal start time must fall on an hour or half-hour between 0 and 24, for example 8.5 is 8:30am. Please try again.")
            print()
            pass
    valid_input_02 = False
    while valid_input_02 == False:
        meal_end = input("When will this meal end? ")
        try:
            float(meal_end)
            try:
                float(meal_end)*2 >= 0 and float(meal_end)*2 <= 48
                valid_input_02 = True
                meal_end = float(meal_end)*2
                print ("meal end time ", meal_end/2)
            except:
                pass
        except:
            print("Meal end time must fall on an hour or half-hour between 0 and 24, for example 8.5 is 8:30am. Please try again.")
            print()
            pass
    
    #print(type(meal_end))
    new_meal = meal_start, meal_end
    print(type(new_meal))
    data_struct[user_name]['meals'].append([meal_start, meal_end])
    print(data_struct)
    data_struct[user_name]['meals'].sort()
    index_of_input = 0
    for i in range(len(data_struct[user_name]['meals'])):
        if data_struct[user_name]['meals'][i] == (meal_start,meal_end):
            index_of_input = i
    if index_of_input == 0:
        a = 0
        b = 0
        index_tuple = data_struct[user_name]['meals'][index_of_input]
        c,d = index_tuple
        print(index_tuple)
    else:
        pre_index_tuple = data_struct[user_name]['meals'][index_of_input - 1]
        a,b = pre_index_tuple
        index_tuple = data_struct[user_name]['meals'][index_of_input]
        c,d = index_tuple
    try:
        post_index_tuple = data_struct[user_name]['meals'][index_of_input + 1]
        e,f = post_index_tuple
    except:
            e = meal_end + 1
            f = e
    float(c)
    float(b)
    float(d)
    float(e)
    if c < b or d > e:
        del data_struct[user_name]['meals'][index_of_input]

    return data_struct

def modify_meal(data_struct):
    which_meal=['\t1. First', '\t2. Second', '\t3. Third', '\t4. Fourth']
    print('═'*120)
    print("\t\t\t\tModify A Mealtime")
    print()
    while True:
        which_user = input("Which user's meal schedule would you like to modify? ")
        if which_user in data_struct:
            break
        else:
            print("That user is not yet registered, please try again")

    print()
    for x in range(len(data_struct[which_user]['meals'])):
        meal = data_struct[which_user]['meals'][x]
        start_meal,end_meal = meal
        print(which_meal[x], " ", start_meal / 2, end_meal /2)
    print()
    meal_index = int(input("Which meal would you like to modify? "))

    if meal_index == 0 or meal_index > (len(data_struct[which_user]['meals'])):
        print("Please enter the number corresponding to the meal you would like to modify.")
    else:
        meal_index = meal_index - 1

    valid_input_01 = False
    while valid_input_01 == False:
        meal_start = input("Enter new starting time of meal: ")
        if meal_start.isdigit() and float(meal_start)*2 >= 0 and float(meal_start)*2 <= 48:
            valid_input_01 = True
            meal_start = float(meal_start)*2
        else:
            print("Meal start time must fall on an hour or half-hour between 0 and 24, for example 8.5 is 8:30am. Please try again.")
            print()
    valid_input_02 = False
    while valid_input_02 == False:
        meal_end = input("Enter new ending time of meal: ")
        if meal_end.isdigit() and float(meal_end)*2 >= 0 and float(meal_end)*2 <= 48 and float(meal_end) > float(meal_start)/2:
            valid_input_02 = True
            meal_end = float(meal_end)*2
        else:
            print("Meal end time must be after start, and fall on an hour or half-hour between 0 and 24, for example 8.5 is 8:30am. Please try again.")
            print()

    new_meal = meal_start,meal_end
    data_struct[which_user]['meals'][int(meal_index)] = new_meal
    data_struct[user_name]['meals'].sort()

    for i in range(len(data_struct[user_name]['meals'])):
        if data_struct[user_name]['meals'][i] == (meal_start,meal_end):
            index_of_input = i
    if index_of_input == 0:
        a = 0
        b = 0
        index_tuple = data_struct[user_name]['meals'][index_of_input]
        c,d = index_tuple
        print(index_tuple)
    else:
        pre_index_tuple = data_struct[user_name]['meals'][index_of_input - 1]
        a,b = pre_index_tuple
        index_tuple = data_struct[user_name]['meals'][index_of_input]
        c,d = index_tuple
    try:
        post_index_tuple = data_struct[user_name]['meals'][index_of_input + 1]
        e,f = post_index_tuple
    except:
            e = meal_end + 1
            f = e
    if c < b or d > e:
        del data_struct[user_name]['meals'][index_of_input]
        print("This modification cannot be made because it would conflict with another mealtime.")
    ok = input("Now returning to main menu, press enter to proceed.")
    return data_struct

def save(data_struct):
    print('═'*120)
    print()
    print("\t\t\t\tSave schedule to file")
    output_file_name = input("Choose a name to save schedule as: ")
    os.system('mkdir -p ./Schedules')
    output_file_name = './Schedules/' + output_file_name
    string_format_data = json.dumps(data_struct)
    output_file_handle = open(output_file_name, 'w+')
    output_file_handle.write(string_format_data)
    output_file_handle.close()
    ok = input("Schedule saved to file. Now returning to main menu, press enter to proceed.")
    return

def load():
    print('═'*120)
    print()
    print("\t\t\t\tLoad schedule from file")
    print("Choose a file to load.")
    print()
    schedules_available = (os.listdir('./Schedules'))
    if len(schedules_available) > 0:
        for x in range(len(schedules_available)):
            Schedule = schedules_available[x]
            print(" ", x+1 , ". ", Schedule, sep='')
    print()
    valid_input_04 = False
    while valid_input_04 == False:
        file_to_read = input("Enter the number corresponding to the file you would like to restore to: ")
        try:
            file_to_read = int(file_to_read)
            valid_input_04 = True
        except:
            pass
    file_to_read -= 1
    file_to_read = schedules_available[file_to_read]
    file_to_read = './Schedules/' + file_to_read
    file_contents = open(file_to_read)
    data = file_contents.read()
    data_struct = json.loads(data)
    file_contents.close()
    return data_struct



def next_action():
    data = {}
    while True:
        choice = menu()
        if choice == '1':
            data = create_user(data)
        if choice == '2':
            data = modify_meal(data)
        if choice == '3':
            data = add_meal(data)
        if choice == '4':
            remove_meal(data)
        if choice == '5':
            remove_user(data)
        if choice  == '6':
            data = print_data(data)
        if choice == '7':
            save(data)
        if choice == '8':
            data = load()
        if choice == '9':
            exit()

 

def main():
    next_action()
    

if __name__ == '__main__':
    main()
