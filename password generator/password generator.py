import string
import secrets
import random


AL=string.ascii_lowercase
AU=string.ascii_uppercase
D=string.digits
S=string.punctuation
p=AL+D+S+AU
r=secrets.choice(AL)+secrets.choice(D)+secrets.choice(S)+secrets.choice(AU)
min=12
'''minimum 12 character password required for safety'''
N=int(input('enter password length:'))
if N<=min:
    N=min
password = ''.join(secrets.choice(p) for i in range(N-4))
p=password+r


random.shuffle(list(p))
k=str(p)

print(k)