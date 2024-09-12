from calc_function import do_addition, do_subtraction
from multiply import do_multiplication


def main():
    print('Welcome to the Calculator App')
    print("""
Select the function from the given options:
1. Add
2. Subtract
3. multiplication
""")
    
    user_input = input("Select the function: ")

    a = int(input("Value of A: "))
    b = int(input("Value of B: "))

    if user_input == "1":
        result = a + b
    elif user_input == "2":
        result = a - b
    elif user_input == "3":
        result = a * b
    else:
        result = "Invalid option selected"

    print('Result:', result)

if __name__ == "__main__":
    main()
