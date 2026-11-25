import os
import json

USER_FILE = "user_data.txt"

def setup_user_profile():
    # This method checks if the user previously went through the prompts or not (that way
    #, every time the user opens the app they don't have to go through the full prompt)
    # For now it checks if user_data.txt exists (ie. the file was created, the user went 
    # through the first-time prompts) but in the future it's gonna use something like localstorage

    if os.path.exists(USER_FILE):
        print("\nPETE'S PLATE IS A WORK IN PROGRESS :)\n") # this is a place-holder. Nothing yet
        return # and nothing else, because WIP

    # Our first-time user profile setup
    print("Welcome to Purdue Pete's Plate Setup!")
    weight_lbs = float(input("Enter your weight (in lbs): "))
    height_in = float(input("Enter your height (in inches): "))
    age = int(input("Enter your age: "))
    gender = input("Gender (M/F): ").strip().upper()
    
    print("\nWhat is your current goal?")
    print("1: CUT (-500 cal)")
    print("2: BULK (+500 cal)")
    print("3: MAINTAIN")
    goal_choice = input("Enter 1, 2, or 3: ").strip()
    
    meals_per_day = int(input("\nHow many meals a day do you usually eat? (e.g., 3): "))

    # Converting it to non-boogey rest-of-the-world measurement system
    # For our tdee calculations, this is for the "recommended meals" section later on
    weight_kg = weight_lbs / 2.20462
    height_cm = height_in * 2.54
    
    if gender == 'M':
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
        
    tdee = bmr * 1.375 # Baseline 6,000 steps multiplier (assuming student gets atleast 6k steps a day)
    
    if goal_choice == '1':
        target_calories = tdee - 500
    elif goal_choice == '2':
        target_calories = tdee + 500
    else:
        target_calories = tdee
        
    # Macro Split: 1g protein/lb, 25% calories from fat, remainder carbs
    protein_g = weight_lbs * 1.0
    fat_g = (target_calories * 0.25) / 9
    carbs_g = (target_calories - (protein_g * 4) - (fat_g * 9)) / 4
    
    # Storage (user doesn't have to re-enter)
    user_profile = {
        "weight_lbs": weight_lbs,
        "height_in": height_in,
        "age": age,
        "gender": gender,
        "goal_choice": goal_choice,
        "meals_per_day": meals_per_day,
        "target_calories": round(target_calories),
        "target_protein_g": round(protein_g),
        "target_carbs_g": round(carbs_g),
        "target_fat_g": round(fat_g)
    }

    # Here we create user_data.txt (thats what we used above to check if it is 
    # a first-time user or a returning user)
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(user_profile, f, indent=4)
        
    print("\nSuccess")
    print("\nPETE'S PLATE IS A WORK IN PROGRESS :)\n")

if __name__ == "__main__":
    setup_user_profile()