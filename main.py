import random
print("Welcome to the Password Generator made by the Wati-Dev")
print('''Select which characters you want in the password:
            
            (1) Numbers (123456789)
            (2) Uppercase Letters (ABC...)
            (3) Lowercase Letters (abc...)
            (4) Symbols (!@#$%&*_-+=...)
''')

rep = input("Choice :")

L = []
for i in rep:
    L.append(i)

nums = '0123456789'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = upper.lower()
symbols = '!@#$%&*-_=+/.,;:*~'

nu, up, lo, sy = False, False, False, False

every = ""

for y in L:
    if '1' in L:
        nu = True
    if '2' in L:
        up = True
    if '3' in L:
        lo = True
    if '4' in L:
        sy = True

if nu:
    every += nums
if up:
    every += upper
if lo:
    every += lower
if sy:
    every += symbols
print("\nSelect the length of the password")
length = int(input("Cannot exceed " + str(len(every)) + " characters :"))

print('Here are your passwords :')

for i in range(10):
    password = "".join(random.sample(every, length))
    print(password)
