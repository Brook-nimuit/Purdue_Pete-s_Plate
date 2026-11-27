import json
from parser import parse_menu_data # Imports the data from user.py's script

def get_recommendation():
    # load user data
    try:
        with open("user_data.txt", "r", encoding="utf-8") as f:
            user = json.load(f)
    except FileNotFoundError:
        print("Run the onboarding script first!") # Just in case it is ever run without finishing the prompts first
        return

    # Calculate per-meal budget, defaults to 3 meals /2500 clas
    meals = user.get("meals_per_day", 3)
    meal_cals = user.get("target_calories", 2500) / meals  #Try to get it equal
    
    # get parsed meal data (breakfast only for now)
    breakfast_items = parse_menu_data("tower_menu_data.txt")
    
    # sort items by protein (most important macro IMO)
    def get_protein(item):
        p = item.get("protein_g", "0")
        # Chartwells sometimes writes "less than 1 gram", so we safely convert to float
        try:
            return float(p)
        except ValueError:
            return 0.0
            
    breakfast_items.sort(key=get_protein, reverse=True)
    
    # This is our "greedy algorithm"
    plate = []
    current_cals = 0
    current_protein = 0
    
    for food in breakfast_items:
        try:
            food_cals = float(food.get("calories", 0))
        except ValueError:
            food_cals = 0.0
            
        # If adding this food keeps us under the meal's calorie budget, put it on the plate
        if current_cals + food_cals <= meal_cals:
            plate.append(food)
            current_cals += food_cals
            current_protein += get_protein(food)
            
    # Display the result
    print(f"\n--- Pete's plate ---")
    
    # Map the goal_choice back to a readable word
    goal_map = {"1": "CUT", "2": "BULK", "3": "MAINTAIN"}
    goal_word = goal_map.get(user.get("goal_choice", "3"), "MAINTAIN")
    
    print(f"Goal: {goal_word} | Meal Budget: ~{int(meal_cals)} cals\n")
    
    for item in plate:
        print(f"- {item['name']} ({item['calories']} cals, {item['protein_g']}g protein)")
        
    print(f"\nTotal Plate: {int(current_cals)} cals | {int(current_protein)}g protein")
    print("-------------------------------------------\n")
    return plate

if __name__ == "__main__":
    get_recommendation()
