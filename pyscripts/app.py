import json
from parser import parse_menu_data
from recommendations import get_recommendation

# this is our main user interface. Displays recommended meals first, then actual menu underneath it

def display_full_menu():
    print("\n--- FULL TOWER DINING BREAKFAST MENU ---")
    menu_items = parse_menu_data("tower_menu_data.txt")
    
    # Enumerate makes it easy to assign a loggable number to each item
    # Our user logs meals by inputting numbers, for now
    for index, item in enumerate(menu_items, start=1):
        print(f"[{index}] {item['name']} | {item['calories']} cals | {item['protein_g']}g P | {item['carbs_g']}g C | {item['fat_g']}g F")
    print("----------------------------------------\n") # cleaner read

def main():
    # Print the recommended plate at the top
    get_recommendation()
    
    # Print the full menu right underneath (user can check out other options)
    display_full_menu()
    
    # User logs meals (WIP)
    choice = input("Enter the number of the meal you want to log (or 'q' to quit): ").strip()
    if choice.lower() != 'q':
        print(f"\nSuccessfully logged meal #{choice}! PETE'S PLATE IS A WORK IN PROGRESS :)")

if __name__ == "__main__":
    main()