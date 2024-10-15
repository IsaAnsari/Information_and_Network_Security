import hashlib

result = hashlib.md5(b'BNN College')
result1 = hashlib.md5(b'bnn college')

print("The Byte Equivalent of hash is : ",end="")
print(result.digest())

print("The Byte Equivalent of hash is : ",end="")
print(result1.digest())
