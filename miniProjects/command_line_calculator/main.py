from calc.interface import parse_args, dispatch

def main():
    args = parse_args()
    try:
        result = dispatch(args)
        print(f"✅ Result: {result}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
