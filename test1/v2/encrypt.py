from steganocryptopy.steganography import Steganography

# 스테가노에 사용되는 2차 해시값 생성
  # 키는 Fernet.generate_key()를 통해서 만들어진다 여기서 Fernet은 대칭키 기반 암호화 과정이다.
Steganography.generate_key("../key/key")

# 2차 해시값 + 원본이미지 + 1차 해시값(숨겨지는 데이터)
encrypted = Steganography.encrypt("../key/key","../img/nomal.png",  "../encrypt/encrypt.txt")

# 암호화된 이미지 저장
encrypted.save("../encrypt/secret.png")
