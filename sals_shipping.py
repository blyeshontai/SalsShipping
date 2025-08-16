# Sal's Shipping Project

def calculate_shipping(weight):
    # Ground Shipping
    if weight <= 2:
        cost_ground = weight * 1.5 + 20
    elif weight <= 6:
        cost_ground = weight * 3.00 + 20
    elif weight <= 10:
        cost_ground = weight * 4.00 + 20
    else:
        cost_ground = weight * 4.75 + 20

    # Ground Shipping Premium
    cost_ground_premium = 125.00

    # Drone Shipping
    if weight <= 2:
        cost_drone = weight * 4.5
    elif weight <= 6:
        cost_drone = weight * 9.00
    elif weight <= 10:
        cost_drone = weight * 12.00
    else:
        cost_drone = weight * 14.25

    return cost_ground, cost_ground_premium, cost_drone

# Get user input
weight = float(input("Enter the weight of your package (lb): "))

# Calculate shipping costs
cost_ground, cost_ground_premium, cost_drone = calculate_shipping(weight)

# Display the costs
print("\nShipping Costs:")
print(f"Ground Shipping: ${cost_ground:.2f}")
print(f"Ground Shipping Premium: ${cost_ground_premium:.2f}")
print(f"Drone Shipping: ${cost_drone:.2f}")
