# Go THROUGH our scraped file (all of them have the same structure) to get the macros we want, for example
import json

def parse_menu_data(filepath):
    # this loads the JSON file back into a Python dictionary
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    breakfast_collection = []

    categories = data.get("period", {}).get("categories", []) # our tower_menu_data.txt has 
    # separate "categories" for each meal, some for example are from the buffet and others you order
    # from the grill

    # this loops through each category, and then loop through the food items inside
    for category in categories:
        items = category.get("items", []) # Each category has a list of food items inside

        for item in items:
            # 4. Grab the easy top-level stuff
            food_name = item.get("name")
            calories = item.get("calories")
            
            # Set default macros in case a food item is missing them
            protein = "0"
            carbs = "0"
            fats = "0"

            # Macros for "item", which is our project's goal data, lies withing "nuitrents"
            # in our file
            # We loop through it and grab only the values we care about for this project.
            # For the MVP I'm skipping stuff like "gluten free", "vegan" ...
            for nutrient in item.get("nutrients", []):
                if nutrient.get("name") == "Protein (g)":
                    protein = nutrient.get("value")
                elif nutrient.get("name") == "Total Carbohydrates (g)":
                    carbs = nutrient.get("value")
                elif nutrient.get("name") == "Total Fat (g)":
                    fats = nutrient.get("value")
            
            # Our actual database (a dictionary) ... 
            clean_item = {
                "name": food_name,
                "calories": calories,
                "protein_g": protein,
                "carbs_g": carbs,
                "fat_g": fats
            }
            # stored in our "breakfast_collection (mock data)"
            breakfast_collection.append(clean_item)
            
    return breakfast_collection

if __name__ == "__main__":
    parsed_breakfast = parse_menu_data("tower_menu_data.txt")
    for meal in parsed_breakfast[:5]: # just to check
        print(meal)