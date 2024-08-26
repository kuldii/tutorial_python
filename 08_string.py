a = "hello"
a = 'hello'

a = "joni's house"
a = 'joni\'s house'

b = """hello, my name is
                kuldii."""
b = '''hello, my name is
                kuldii.'''


c = "hello kuldii" # String ber-index (mulai dari index ke-0)

print(c[0]) # <--- h
print(c[1]) # <--- e
print(c[5]) # <--- (spasi)
print(c[6]) # <--- k


print(c[3:]) # <--- lo kuldii
print(c[3:9]) # <--- lo kul

print(c[-3:]) # <--- hello kuldiihello kuldii


# MODIFY STRING

print(c.replace("i", "x"))

c = "     kuldii aaaa     "
print(c.strip())

age = 20 + 2
text = f"I am {age} years old"


print(c.split(" "))