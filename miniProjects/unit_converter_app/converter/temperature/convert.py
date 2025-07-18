def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return f"{value}°{from_unit.upper()} = {value}°{to_unit.upper()}"

    if from_unit == "c":
        if to_unit == "f":
            return f"{value}°C = {(value * 9/5) + 32:.2f}°F"
        elif to_unit == "k":
            return f"{value}°C = {value + 273.15:.2f}K"
    elif from_unit == "f":
        if to_unit == "c":
            return f"{value}°F = {(value - 32) * 5/9:.2f}°C"
        elif to_unit == "k":
            return f"{value}°F = {(value - 32) * 5/9 + 273.15:.2f}K"
    elif from_unit == "k":
        if to_unit == "c":
            return f"{value}K = {value - 273.15:.2f}°C"
        elif to_unit == "f":
            return f"{value}K = {(value - 273.15) * 9/5 + 32:.2f}°F"

    return "⚠️ Invalid temperature unit."