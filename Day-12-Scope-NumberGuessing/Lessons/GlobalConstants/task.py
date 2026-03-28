#Global Constants
PI = 3.14159
GRAVITY = 9.81
def calculate_circumference(radius):
    return 2 * PI * radius

def calculate_weight(mass):
    return mass * GRAVITY

# Example usage
radius = 5
mass = 10

circumference = calculate_circumference(radius)
weight = calculate_weight(mass)

print(f"Circumference of the circle with radius {radius}: {circumference}")
print(f"Weight of an object with mass {mass} kg: {weight} N")