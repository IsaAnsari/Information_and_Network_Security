import hashlib

Str = input("Enter the Value to encode : ")
result = hashlib.sha1(Str.encode())

print("The Hexadecimal Equivalent is SHA1 is : ")
print(result.hexdigest())
