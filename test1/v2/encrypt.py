from steganocryptopy.steganography import Steganography

Steganography.generate_key("../key/key")

encrypted = Steganography.encrypt("../key/key","../img/nomal.png",  "../encrypt/encrypt.txt")

encrypted.save("../encrypt/secret.png")
