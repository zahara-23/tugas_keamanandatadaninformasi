from math import gcd

class AffineCipher:
    def __init__(self, a, b):
        
        if gcd(a, 26) != 1:
            raise ValueError("a harus relatif prima dengan 26 agar punya invers")
        self.a = a
        self.b = b
        self.m = 26  

    def mod_inverse(self, a, m):
        """Mencari invers a mod m dengan Extended Euclidean Algorithm"""
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None

    def enkripsi(self, x):
        """x adalah indeks huruf (0-25)"""
        return (self.a * x + self.b) % self.m

    def dekripsi(self, y):
        """y adalah indeks huruf (0-25)"""
        a_inv = self.mod_inverse(self.a, self.m)
        return (a_inv * (y - self.b)) % self.m

    def encrypt_text(self, text):
        """Enkripsi teks huruf besar"""
        result = ""
        for char in text.upper():
            if char.isalpha():
                x = ord(char) - ord('A')
                enc = self.enkripsi(x)
                result += chr(enc + ord('A'))
            else:
                result += char
        return result

    def decrypt_text(self, text):
        """Dekripsi teks huruf besar"""
        result = ""
        for char in text.upper():
            if char.isalpha():
                y = ord(char) - ord('A')
                dec = self.dekripsi(y)
                result += chr(dec + ord('A'))
            else:
                result += char
        return result



cipher = AffineCipher(5, 8)   
plain = "HELLO"
encrypted = cipher.encrypt_text(plain)
decrypted = cipher.decrypt_text(encrypted)

print("Plaintext :", plain)
print("Terenkripsi :", encrypted)
print("Terdekripsi :",decrypted)