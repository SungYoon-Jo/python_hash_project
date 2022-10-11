import sys
import hashlib
 
if sys.version_info < (3, 6):
    import sha3
 

str = input("input text : ")
 
hash_sha256 = hashlib.new("sha256", str.encode())
# h = list(hash_sha256.hexdigest())
h = hash_sha256.hexdigest()

# result = []
# for i in range(0,len(h),2):
#     result.append(h[i:i+2])
# print(result)


# print("\nSHA3-512 Hash: ", len(h))

f = open("../encrypt/encrypt.txt", "w")
f.write(h)
f.close()

print("\nsha256 Hash: ", h)
print("\nsha256 Hash: ", len(h))