def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (discount_percent/100)
    return price

marked_price = float(input("Enter the Marked Price: "))
discount = float(input("Enter the discount percentage: "))

buying_price = calculate_discount (marked_price, discount)

if discount >= 20:
    print(f"Your Total Cost is: {buying_price}")

else:
    print(f"No discount applied. Price remains: {buying_price}")