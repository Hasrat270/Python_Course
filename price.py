originalPrice = input("Enter the original price: ")
discountPercentage = input("Enter the discount percentage: ")


discountedPrice = float(originalPrice) * (1 - float(discountPercentage) / 100)
print(f"The price after a discount of {discountPercentage}% is: ${discountedPrice}")