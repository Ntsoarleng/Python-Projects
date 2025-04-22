### Approximate burnt calories per minute when workouts are done moderately
workouts = {"running": 10.8,
            "cycling": 7.5,
            "jumprope": 12,
            "weightlifting": 4.5,
            "crossfit": 10,
            "pilates": 5.5,
            "yoga": 4.75,
            "swimming": 9,
            "dancing": 7,
            "hiking": 6.5}

#The function below will take the workout type and the total time spent in minutes on that workout to calculate the approximate total of calories burnt
def total_calories_burnt(workout_type, time_spent):
    if workout_type in workouts:
        burnt_calories = time_spent * workouts[workout_type]
        return burnt_calories
    else:
        return 0


print("Once you have entered all the workouts you did, type 'done' when you get another prompt. \n")
workout_log = {}

while True:
    workout = input("Enter any workout in the workouts dictionary: ").lower()
    
    if workout == "done":
        break

    if workout not in workouts:
        print("Invalid Input! Please enter a valid workout from the workouts dictionary.\n")
        continue

    duration = float(input("Enter the total workout time in minutes: "))
    
    workout_log[workout] = duration

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
print("Your workout log is as follows: ")

for key, value in workout_log.items():
    print(f"{key}: {value} minutes")

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")

total_calories = 0
for workout, duration in workout_log.items():
    if workout in workouts:
        total_calories += total_calories_burnt(workout, duration)

kgs = round(total_calories/7700, 3)
print(f"Congratulations! You burnt a total of {total_calories} calories.")
print(f"Estimated weight loss: {kgs} kg.\n")
print("Keep going... You got this!\n")
