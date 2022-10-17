from steganocryptopy.steganography import Steganography

# 2차 해시값 + 암호 데이터가 숨겨진 이미지를 가지고 복호화 함
decrypted_text = Steganography.decrypt("../key/key", "../encrypt/secret.png")

print(decrypted_text)

# 복호화 된 키값을 텍스트로 저장
Steganography.write_file("../decrypt/decrypt.txt", decrypted_text)