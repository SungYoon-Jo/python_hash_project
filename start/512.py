import sys
import hashlib
 
if sys.version_info < (3, 6):
    import sha3
 
str = "good"
 
hash_sha3_512 = hashlib.new("sha3_512", str.encode())
h = list(hash_sha3_512.hexdigest())
 
# result = []
# for i in range(0,len(h),2):
#     result.append(h[i:i+2])
# print(result)


print("\nSHA3-512 Hash: ", len(h))
