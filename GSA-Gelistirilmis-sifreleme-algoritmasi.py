import random

# Sezar şifreleme algoritması
def caesar_encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        encrypted_char = chr((ord(char) + shift - 32) % 94 + 32)
        print(encrypted_char)

        result += encrypted_char
    return result

def caesar_decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        decrypted_char = chr((ord(char) - shift - 32) % 94 + 32)
        result += decrypted_char
    return result

# Simetrik şifreleme algoritması
def symmetric_encrypt(text, key):
    random.seed(key) 
    keylist = list(range(256))
    random.shuffle(keylist)
    keylist = bytes(keylist)
    result = bytearray()
    for i in range(len(text)):
        result.append(text[i] ^ keylist[i % 256])
    return result

def symmetric_decrypt(text, key):
    random.seed(key)
    keylist = list(range(256))
    random.shuffle(keylist)
    keylist = bytes(keylist)
    result = bytearray()
    for i in range(len(text)):
        result.append(text[i] ^ keylist[i % 256])
        print(result)
    return result

# Yeni algoritma
def custom_encrypt(text, shift, key):
    encrypted_text = caesar_encrypt(text, shift)
    result = symmetric_encrypt(encrypted_text.encode(), key)
    return result.hex()

def custom_decrypt(text, shift, key):
    text_bytes = bytes.fromhex(text)
    decrypted_text = symmetric_decrypt(text_bytes, key).decode()
    result = caesar_decrypt(decrypted_text, shift)
    return result

# Kullanım örneği
text = "Merhaba"
shift = 6
key = "AglasunMYO"

encrypted_text = custom_encrypt(text, shift, key)
print("Şifrelenmiş metin:", encrypted_text)

decrypted_text = custom_decrypt(encrypted_text, shift, key)
print("Çözülmüş metin:", decrypted_text)