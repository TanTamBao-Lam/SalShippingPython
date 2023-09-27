weight = 41.5

# Ground shipping
if weight <= 2:
    cost = weight * 1.50 + 20.00
elif 2 < weight <= 6:
    cost = weight * 3.00 + 20.00
elif 6 < weight <= 10:
    cost = weight * 4.00 + 20.00
else:
    cost = weight * 4.75 + 20.00

print("Ground Shipping cost")
print(cost)

# Premium Ground Shipping
premium_cost = 125.00
print("Premium Shipping cost: ")
print(premium_cost)

# Drone Shipping
if weight <= 2:
    cost = weight * 1.50 + 0
elif 2 < weight <= 6:
    cost = weight * 3.00 + 0
elif 6 < weight <= 10:
    cost = weight * 4.00 + 0
else:
    cost = weight * 4.75 + 0

print("Drone Shipping cost: ")
print(cost)