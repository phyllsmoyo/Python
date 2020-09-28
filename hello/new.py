t_date = input("Today's date?\n")
b_fast = int(input("Breakfast calories?\n"))
lunch = int(input("Lunch calories?\n"))
dinner = int(input("Dinner calories?\n"))
snack = int(input("Snack calories?\n"))
sum_calorie = b_fast + lunch + dinner + snack

print("Calorie content for " + (t_date) + ":" + str(sum_calorie))
