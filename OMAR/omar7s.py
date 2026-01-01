import math

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

# Function to calculate the volume of a sphere
def calculate_sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

while True:
    print("Choose an option:")
    print("1. Calculate the area of a circle")
    print("2. Calculate the volume of a sphere")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        radius = float(input("Enter the radius of the circle: "))
        area = calculate_circle_area(radius)
        print(f"The area of the circle is: {area:.2f}")
    elif choice == '2':
        radius = float(input("Enter the radius of the sphere: "))
        volume = calculate_sphere_volume(radius)
        print(f"The volume of the sphere is: {volume:.2f}")
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
