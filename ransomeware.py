import base64
from Crypto.Cipher import AES 
import sys,os, random, struct, glob

def cbc_encrypt(plaintext: str, key: str):

    block_size = len(key)
    padding = (block_size - len(plaintext) % block_size) or block_size  # 填充字节

    iv = "my name is IV123"
    mode = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
    ciphertext = mode.encrypt((plaintext + padding * chr(padding)).encode())

    return base64.b64encode(iv.encode() + ciphertext).decode()


def cbc_decrypt(ciphertext: str, key: str):
    ciphertext = base64.b64decode(ciphertext)
    mode = AES.new(key.encode(), AES.MODE_CBC, ciphertext[:AES.block_size])
    plaintext = mode.decrypt(ciphertext[AES.block_size:]).decode()
    return plaintext[:-ord(plaintext[-1])]


startPath = '/home/parallels/Desktop/coin.png'
if __name__ == '__main__':
    key = "my name is key12" 
	
    ciphertext = cbc_encrypt('hello', key)
    print(ciphertext)

    plaintext = cbc_decrypt(ciphertext, key)
    print(plaintext)
