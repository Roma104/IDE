###
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y)

# swap the values
#using and additional variable to hold the value, so it wouldn't just disapear
z = y
#swapping first variable with the second one
y = x
#pulling the left variable back to our pool
x = z

print("After swapping: x=", x, "y=", y)