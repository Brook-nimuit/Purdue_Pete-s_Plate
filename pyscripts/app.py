import json
from datetime import datetime
from parser import parse_menu_data
from recommendations import get_recommendation

def log_meals(selected_items):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "timestamp": timestamp,
        "items": selected_items
    }
    
    # Check if the log file exists, load it, append the new entry, and save it back
    try:
        with open("logged_meals.json", "r", encoding="utf-8") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []
        
    logs.append(log_entry)
    
    with open("logged_meals.json", "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)
        
    print(f"\nSuccess! Logged {len(selected_items)} item(s) at {timestamp}.")

def display_full_menu():
    print("\n--- FULL TOWER DINING BREAKFAST MENU ---")
    menu_items = parse_menu_data("tower_menu_data.txt")
    
    # Offset the index by 2, leaving 1 reserved for the Recommended Plate
    for index, item in enumerate(menu_items, start=2):
        print(f"[{index}] {item['name']} | {item['calories']} cals | {item['protein_g']}g P")
    print("----------------------------------------\n")
    return menu_items

def main():
    # 1. Print the recommended plate and capture the data
    recommended_plate = get_recommendation()
    
    # 2. Print the full menu and capture the data
    menu_items = display_full_menu()
    
    # 3. Terminal logging interface
    print("[1] Log the entire Recommended Plate")
    print("[2+] Log individual items (comma-separated, e.g., 2, 5, 8)")
    
    choice = input("\nEnter your choice (or 'q' to quit): ").strip()
    
    if choice.lower() == 'q':
        return
        
    selected_items = []
    
    if choice == '1':
        selected_items = recommended_plate
    else:
        try:
            # Parse comma-separated inputs
            indices = [int(x.strip()) for x in choice.split(",")]
            for idx in indices:
                # Subtract 2 because our display index started at 2
                if 2 <= idx <= len(menu_items) + 1:
                    selected_items.append(menu_items[idx - 2])
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")
            return
            
    if selected_items:
        log_meals(selected_items)
        print("PETE'S PLATE IS A WORK IN PROGRESS :)")
    else:
        print("No valid items selected.")

if __name__ == "__main__":
    main()