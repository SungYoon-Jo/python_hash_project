import hashlib
 
# 1차 소스 = 사용자 텍스트 입력
str = input("input text : ")
 
# hash256 해시 알고리즘 선정 및 인코딩 컴퓨터 저장시 바이트 변환작업
hash_sha256 = hashlib.new("sha256", str.encode())

# 위에서 입력받은 데이터를 가지고 해시값을 생성함
h = hash_sha256.hexdigest()

# 해시값 텍스트 저장
f = open("../encrypt/encrypt.txt", "w")
f.write(h)
f.close()

# 해시값 확인
print("\nsha256 Hash: ", h)
# 해시값 길이 확인
print("\nsha256 Hash: ", len(h))


## 해시값 인덱스 슬라이싱
# result = []
# for i in range(0,len(h),2):
#     result.append(h[i:i+2])
# print(result)
