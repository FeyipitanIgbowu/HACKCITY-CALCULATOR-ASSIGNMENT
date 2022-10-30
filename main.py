
print("WELCOME TO SIMPLE CALCULATOR")
first_value = input("Enter the first value: ")
second_value = input("Enter the second value: ")
first_value_change = int(first_value)
second_value_change = int(second_value)

addition = first_value_change + second_value_change
print(f"Sum: {addition}")

subtratction = first_value_change - second_value_change
print(f"Subtratction: {subtratction}")

multiplication = first_value_change * second_value_change
print(f"Multiplication: {multiplication}")

division = first_value_change / second_value_change
print(f"Division: {division}")

import math
exponential = math.exp(addition)
print(f"Exponential: {exponential}")

square_root = math.sqrt(addition)
print(f"Squareroot: {square_root}")
