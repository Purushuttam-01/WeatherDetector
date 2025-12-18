import random

weather_conditions = [
    "Sunny", "Cloudy", "Rainy", "Stormy", "Clear", "Windy", "Humid"
]

def get_weather(city):
    condition = random.choice(weather_conditions)
    temperature = random.randint(15, 40)
    humidity = random.randint(20, 90)

    return {
        "city": city.title(),
        "condition": condition,
        "temperature": temperature,
        "humidity": humidity
    }
