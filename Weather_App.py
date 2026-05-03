import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
API_KEY = os.getenv("API_KEY")

def get_weather(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        response = requests.get(url)
        data = response.json()

        # Error handling
        if data["cod"] != 200:
            print("❌ City not found! Please enter valid city.")
            return

        # Extract data
        city_name = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]

        # Display result
        print("\n🌍 City:", city_name)
        print("🌡️ Temperature:", temp, "°C")
        print("💧 Humidity:", humidity, "%")
        print("☁️ Condition:", condition)

    except Exception as e:
        print("⚠️ Error:", e)


# Main program
city = input("Enter city name: ")
get_weather(city)