def convert_length(value, from_unit, to_unit):
    units = {
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "inch": 0.0254,
        "ft": 0.3048,
        "mi": 1609.34
    }

    try:
        base_value = value * units[from_unit]
        converted = base_value / units[to_unit]
        return f"{value} {from_unit} = {converted:.2f} {to_unit}"
    except KeyError:
        return "⚠️ Invalid length unit."
