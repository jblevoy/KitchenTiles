
import time

jasen_meal_now = False
jasen_meal_over = False
jasen_meal_pre = False
tod_48 = 0
sumner = {'jasen': {'meals': [[5, 10], [20, 25]]}, 'sam': {'meals': [[20.0, 38.0]]}, 'bri': {'meals': [[12.0, 29.4]]}}

while True:
    print("tod_48 ", tod_48)
    tod_48 += 1
    time.sleep(.5)
    for user in sumner.keys():
        print("user: ", user)
        if user == "jasen":
            user_meals = sumner[user]['meals']
            for each_meal in user_meals:
                meal_start,meal_end = each_meal
                print("each_meal", each_meal)
                if meal_start <= tod_48 and meal_end >= tod_48:
                    jasen_meal_now = True
                    
                    print("meal time ", jasen_meal_now)
#                else:
#                   jasen_meal_now = False
                if tod_48 < meal_end + 3 and tod_48 > meal_end:
                    jasen_meal_over = True
                    print("meal over ", jasen_meal_over)
#                else:
#                    jasen_meal_over = False
                if tod_48 > meal_start - 3 and tod_48 < meal_start:
                    jasen_meal_pre = True
                    print("meal pre ", jasen_meal_pre)
#                else:
#                    jasen_meal_pre = False
