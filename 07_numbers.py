x = 8 # int
y = 8.0 # float
z = 8j # complex


print(x, type(x))
print(y, type(y))
print(z, type(z))


a = 2E3 # float ===> 2 * 10^3
print(a, type(a))

b = -2E3 # float ===> -2 * 10^3
print(b, type(b))


# Conversion

x = float(7)
print(x, type(x))


# Random number

import random

print(random.randrange(0,5)) # ---> 5 exclusive => 0,1,2,3,4