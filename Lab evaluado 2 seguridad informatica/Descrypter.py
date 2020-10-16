from pyDes import *
import binascii



def desC(mensaje):
    k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(mensaje)
    return (binascii.hexlify(d).decode())

def desD(texto):
    k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    return ("Decrypted: %r" % k.decrypt(texto).decode())

def tridesC(mensaje):
    k = triple_des("1234123412341234", ECB, padmode=PAD_PKCS5)
    d = k.encrypt(mensaje)
    return (binascii.hexlify(d).decode())

def tridesD(mensaje):
    k = triple_des("1234123412341234", ECB, padmode=PAD_PKCS5)
    d = k.decrypt(mensaje)
    return (d.decode())
