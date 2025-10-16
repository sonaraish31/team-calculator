# main.py
"""Simple command-line interface for the calculator."""
import sys
try:
    import calculator
    import advanced
except Exception as e:
    print("Error importing modules:", e)
    sys.exit(1)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def menu():
    print("""
Team Calculator
1) Add
2) Subtract
3) Multiply
4) Divide
5) Square root
6) Power
7) Percentage (part of whole)
0) Exit
""")

def main_loop():
    while True:
        menu()
        choice = input("Choose operation: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        if choice in ("1","2","3","4"):
            a = get_number("First number: ")
            b = get_number("Second number: ")
            try:
                if choice == "1":
                    print("Result:", calculator.add(a,b))
                elif choice == "2":
                    print("Result:", calculator.subtract(a,b))
                elif choice == "3":
                    print("Result:", calculator.multiply(a,b))
                elif choice == "4":
                    print("Result:", calculator.divide(a,b))
            except Exception as e:
                print("Error:", e)
        elif choice == "5":
            x = get_number("Number: ")
            try:
                print("Result:", advanced.sqrt(x))
            except Exception as e:
                print("Error:", e)
        elif choice == "6":
            base = get_number("Base: ")
            exp = get_number("Exponent: ")
            print("Result:", advanced.power(base, exp))
        elif choice == "7":
            part = get_number("Part: ")
            whole = get_number("Whole: ")
            try:
                print(f"Result: {advanced.percentage(part, whole):.4f}%")
            except Exception as e:
                print("Error:", e)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_loop()
