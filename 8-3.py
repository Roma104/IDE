###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
#odbiorca wrzuca temperature w st. celcjusza
#
#tworzymy 3 zmienne, odpowiednio: celcjusz, farenhajt i kelvin
#farenhajt przelicza celcjusza na farenhajty przy pomocy znalezionej formóły
#kelvin zachowuje się analogicznie
#
#program wyrzuca nam informacje zwrotną :D
#

celcjusz = int(input("Enter temperature in Celcius: "))

farenhajt = 2 * celcjusz + 32

kelvin = celcjusz + 273.15

print(f'Kelvin: {kelvin}; Fahrenheit: {farenhajt}.')
