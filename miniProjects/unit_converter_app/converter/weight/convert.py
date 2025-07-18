def convert_weight(value, from_unit, to_unit):
    units = {
        "kg": 1,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495
    }

    try:
        base_value = value * units[from_unit]
        converted = base_value / units[to_unit]
        return f"{value} {from_unit} = {converted:.2f} {to_unit}"
    except KeyError:
        return "⚠️ Invalid weight unit."
