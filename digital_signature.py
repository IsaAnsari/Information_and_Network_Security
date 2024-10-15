from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

def generate_Signature(private_key,message):
    key = RSA.importKey(private_key)
    hashed_message = SHA256.new(message.encode("utf-8"))
    Signer = PKCS1_v1_5.new(key)
    Signature = Signer.sign(hashed_message)
    return Signature

def verify_signature(public_key,message,Signature):
    key = RSA.importKey(public_key)
    hashed_message = SHA256.new(message.encode("utf-8"))
    Verifier = PKCS1_v1_5.new(key)
    return Verifier.verify(hashed_message,Signature)

random_generator = Random.new().read
key_pair = RSA.generate(2048,random_generator)
public_key = key_pair.publickey().export_key()
private_key = key_pair.export_key()

Message = "Hello World!"

signature = generate_Signature(private_key,Message)
print("Generated Signature : ",signature)

is_valid = verify_signature(public_key,Message,signature)
print("Result of Generated Signature : ",is_valid)
