# Test Safe Skill
# This is a legitimate weather skill for testing

import os
import json
import urllib.request

def get_weather(city: str) -> dict:
    """Get weather for a city"""
    # Safe: only reads config from designated location
    config_path = os.path.expanduser("~/.config/weather-skill/config.json")
    
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        config = {}
    
    # Safe: uses public API
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}"
    
    try:
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read())
        return data
    except Exception as e:
        return {"error": str(e)}

if __name__ == '__main__':
    print(get_weather("Beijing"))
