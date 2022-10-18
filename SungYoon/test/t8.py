from steganocryptopy.steganography import Steganography

Steganography.generate_key("key")
encrypted = Steganography.encrypt("key","hide.png",  "classified.us")
encrypted.save("Secret.png")