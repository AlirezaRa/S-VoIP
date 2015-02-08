import binascii
from Crypto.Cipher import AES


blocksize = 16
padchar = '\x00'


def pad(x):
    topad = blocksize - (len(x) % blocksize)
    padded = x + topad * padchar
    return padded


def unpad(x):
    return x.rstrip('\x00')


def encrypt(im, key):
    if len(key) % blocksize != 0:
        key = pad(key)
    if len(im) % blocksize != 0:
        im = pad(im)
        cipher = AES.AESCipher(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(im)
    b16 = binascii.hexlify(bytearray(ciphertext))
    return b16


def decrypt(ciphertext, key):
    if len(key) % blocksize != 0:
        key = pad(key)
    ct = binascii.unhexlify(ciphertext)
    cipher = AES.AESCipher(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(ct))
