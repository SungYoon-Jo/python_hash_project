from steganocryptopy.steganography import Steganography

decrypted_text = Steganography.decrypt("key", "../encrypt/secret.png")

print(decrypted_text)

Steganography.write_file("../decrypt/decrypt.txt", decrypted_text)