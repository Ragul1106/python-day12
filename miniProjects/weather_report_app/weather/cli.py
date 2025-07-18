from weather import api as weather_api
from weather import formatter as fmt

def run_cli():
    print("🌦️ Weather Report Console App")
    while True:
        city = input("\nEnter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("👋 Goodbye!")
            break
        data = weather_api.get_weather_data(city)
        report = fmt.format_weather(data)
        print(report)
