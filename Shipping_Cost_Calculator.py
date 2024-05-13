#Shipping Cost Calculator

## Input package weight and shipping rate
Weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate Shipping Cost
shipping_cost = weight * rate
## Display the results
print(f"Shipping Cost: {shipping_cost} USD")
