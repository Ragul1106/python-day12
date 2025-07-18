import argparse
from calc import basic as B
from calc import advanced as A

def parse_args():
    parser = argparse.ArgumentParser(description="🧮 Meenu's CLI Calculator")
    
    subparsers = parser.add_subparsers(dest="command", help="Operations")

    # Basic ops
    for op in ['add', 'subtract', 'multiply', 'divide']:
        sp = subparsers.add_parser(op)
        sp.add_argument("a", type=str)
        sp.add_argument("b", type=str)

    # Advanced ops
    power = subparsers.add_parser("power")
    power.add_argument("base", type=str)
    power.add_argument("exp", type=str)

    sqrt = subparsers.add_parser("sqrt")
    sqrt.add_argument("x", type=str)

    trig = ["sin", "cos", "tan"]
    for fn in trig:
        sp = subparsers.add_parser(fn)
        sp.add_argument("angle", type=str)

    return parser.parse_args()

def dispatch(args):
    cmd = args.command

    match cmd:
        case "add": return B.add(args.a, args.b)
        case "subtract": return B.subtract(args.a, args.b)
        case "multiply": return B.multiply(args.a, args.b)
        case "divide": return B.divide(args.a, args.b)
        case "power": return A.power(args.base, args.exp)
        case "sqrt": return A.sqrt(args.x)
        case "sin": return A.sin(args.angle)
        case "cos": return A.cos(args.angle)
        case "tan": return A.tan(args.angle)
        case _: return "❌ Unknown command"
