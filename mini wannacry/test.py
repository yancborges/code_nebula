import hashlib

# Testing SHA lib

x = input("Message: ")
b = x.hexdigest()
#print(hashlib.sha512(x).hexdigest())
print(hashlib.sha512(b))
