###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')

side_a = int(a)
side_b = int(b)
side_c = int(c)

Voulume = side_a*side_b*side_c

Sufeca_area = 2*(side_a*side_b + side_a*side_c + side_b*side_c)

print(f'The volume of a cuboid with sides {a}, {b} and {c} is {Voulume}')
print(f'The surface area of a cuboid with sides {a}, {b} and {c} is {Sufeca_area}')