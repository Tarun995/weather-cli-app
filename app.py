import sys
from utils import get_weather

def main():
    if len(sys.argv) < 2:
        print("Usage: python app.py <city_name>")
        return

    city = " ".join(sys.argv[1:])
    weather = get_weather(city)
    print(f"🌦 Weather in {city}: {weather}")

if __name__ == "__main__":
    main()
print("💧 Humidity: 60%")
