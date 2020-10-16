import pyDes
import binascii

text = '111122223333AAAA44446666BBBBEEEE'
binaryText = binascii.unhexlify(text)

key = '123412341234ABCD'

k = pyDes.triple_des(key, pyDes.ECB)

encrypted = k.encrypt(binaryText)

print("Encrypted Value = %r" % binascii.hexlify(encrypted))

# decrypted = k.decrypt(encrypted)
# print("Decrypted Value = %r" %binascii.hexlify(decrypted))
