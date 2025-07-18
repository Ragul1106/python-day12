import argparse
from converter.length.convert import convert_length
from converter.weight.convert import convert_weight
from converter.temperature.convert import convert_temperature

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🌐 Unit Converter App")

    parser.add_argument("type", choices=["length", "weight", "temperature"], help="Conversion type")
    parser.add_argument("value", type=float, help="Value to convert")
    parser.add_argument("from_unit", help="Convert from unit")
    parser.add_argument("to_unit", help="Convert to unit")

    args = parser.parse_args()

    if args.type == "length":
        result = convert_length(args.value, args.from_unit, args.to_unit)
    elif args.type == "weight":
        result = convert_weight(args.value, args.from_unit, args.to_unit)
    elif args.type == "temperature":
        result = convert_temperature(args.value, args.from_unit, args.to_unit)
    else:
        result = "Invalid conversion type."

    print(f"✅ Result: {result}")
