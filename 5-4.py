###
#23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. 
#Then, it calculates and prints both the amount and its VAT. 
# Apply formatting with two decimal places.
#


amount_string = input("Amount paid:")

amount = float(amount_string)

vat = amount * 0.23
vat_output = round(vat,2)

print(f'The paid amount was: {amount}, and so VAT is: {vat_output}.')
