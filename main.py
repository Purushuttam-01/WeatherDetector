from weather_data import get_weather

def main():
    print("=== Weather CLI ===")

    while True:
        city = input("\nEnter a city name (or type 'exit'): ")

        if city.lower() == "exit":
            print("Goodbye!")
            break

        if not city.strip():
            print("Please enter a valid city name.")
            continue

        report = get_weather(city)
        
        print(f"\nWeather in {report['city']}:")
        print(f"- Condition: {report['condition']}")
        print(f"- Temperature: {report['temperature']}°C")
        print(f"- Humidity: {report['humidity']}%")

if __name__ == "__main__":
    main()
