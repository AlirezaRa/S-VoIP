import binascii
from Crypto.Cipher import AES
import getpass
import espeakstuff
import gspeechstuff

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


def mainEnc():
    message = str(raw_input("What's your secret message? "))
    key = getpass.getpass("Enter your key (shadowed input): ")
    ciphertext = encrypt(message, key)
    while True:
        choice = str(raw_input("Recite to the other side using (e)Speak or (g)oogle?"))
        if choice == 'e':
            espeakstuff.sayAES(ciphertext)
            break
        elif choice == 'g':
            gspeechstuff.sayAES(ciphertext)
            break
        else:
            "Option unavailable."


def mainDec():
    ciphertext = str(raw_input("What did you hear? "))
    key = getpass.getpass("Enter the key (shadowed input): ")
    message = decrypt(ciphertext, key)
    d = str(raw_input("Show message? (y/n) "))
    if d == 'y':
        print message
    elif d != 'y':
        pass
