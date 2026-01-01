# Function to calculate and display the birth year
def calculate_birth_year(age):
    current_year = 2023  # You can change this to the current year
    birth_year = current_year - age
    return birth_year

try:
    age = int(input("Enter your age: "))
    birth_year = calculate_birth_year(age)
    print(f"Your birth year is approximately {birth_year}.")
except ValueError:
    print("Invalid input. Please enter a valid age (a positive integer).")
