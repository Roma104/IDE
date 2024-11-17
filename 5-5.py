####
#The price of the product on the price tag is given before and after the discount is applied
#Write a program that allows you to enter the product price and discount. 
#Print the product price, discount, discounted product price, and the difference between the product price before and after the discount.
# Print all prices with two decimal places. Sample result:
#

price_input = input("Enter original price: ")
discunt_input = input("Enter your discount % : ")

price = float(price_input)
discount = float(discunt_input)/100
saved_money = round(price*discount,2)
price_after = round(price - saved_money,2)


print(f"Price before {price}.")
print(f"Your discount % {discount}.")
print(f"Price after {price_after}.")
print(f"Money you saved {saved_money}.")