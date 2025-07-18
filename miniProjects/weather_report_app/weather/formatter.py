from datetime import datetime

def format_weather(data):
    if "error" in data:
        return f"❌ Error: {data['error']}"

    name = data["name"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    time = datetime.fromtimestamp(data["dt"]).strftime("%Y-%m-%d %H:%M:%S")

    return (
        f"\n📍 Weather Report for {name}\n"
        f"🕒 Time         : {time}\n"
        f"🌡️ Temperature : {temp}°C\n"
        f"🌥️ Description : {desc.capitalize()}\n"
        f"💧 Humidity    : {humidity}%\n"
        f"🌬️ Wind Speed  : {wind} m/s\n"
    )
