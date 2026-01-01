# Function to get and display the name
def get_and_display_name():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

# Number of times to ask for the name
num_attempts = 3

for _ in range(num_attempts):
    get_and_display_name()
