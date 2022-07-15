#Type Coversion
import string


x = 10
y = 3.14
z = "20"

# "20" = > 20
# string => float(number)
z=float(z)

z=z+50
print (z)

# float(number) => string
z=str(z)

print(type(z))