import time
from itertools import product

target = input("Please set password : ")
chars = 'abcdefghijklmnopqrstuvwxyz'

def check(chars, number):
    pwd = product(chars ,repeat = number)

    for i in pwd:
        if ''.join(i) == target:
            return ''.join(i)
        
start = time.time()

degits = int(input("Please passwoed of number of degits : "))
password = check(chars, degits)

if password == None:
    print("We can't guess your password.")

else:
    print(f"Your password is {password}, isn't it?")

end = time.time()

time = end - start

print(f"We took time to guess your password {time}")