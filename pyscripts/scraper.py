from curl_cffi import requests
import json

TOWER_DINING_URL = "https://apiv4.dineoncampus.com/locations/5873e3933191a200e44efecf/menu" 

headers = {
    'accept': 'application/json',
    'origin': 'https://dineoncampus.com',
    'referer': 'https://dineoncampus.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'x-visitor-id': 'ab171535-5335-4b95-9642-806efa2cce50'
}

params = {
    'date': '2026-11-24',
    'period': '6b06251193c18140627b8965',
    'locale': 'en',
}

def fetch_menu():
    print("Pulling Breakfast data (prototype) from Tower Dining ...")
    try:
        response = requests.get(TOWER_DINING_URL, params=params, headers=headers, impersonate="chrome")
        response.raise_for_status() 
        
        with open("tower_menu_data.txt", "w", encoding="utf-8") as file:
            file.write(json.dumps(response.json(), indent=4))
            
        print("Success saved in .txt file.")
        
    except Exception as e:
        print(f"Failed to scrape data: {e}")

if __name__ == "__main__":
    fetch_menu()