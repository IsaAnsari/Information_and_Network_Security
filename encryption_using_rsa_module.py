import rsa

publickey, privatekey = rsa.newkeys(512)

Message = "Welcome to BNN College"

encMessage = rsa.encrypt(Message.encode(),publickey)
print("Original String: ",Message)
print("Encrypted String: ",encMessage)

decMessage = rsa.decrypt(encMessage,privatekey).decode()
print("Decrypted String: ",decMessage)
