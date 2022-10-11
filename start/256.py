import sys
import hashlib
 
if sys.version_info < (3, 6):
    import sha3
 
str = "good"
 
hash_sha3_256 = hashlib.new("sha3_256", str.encode())
h = list(hash_sha3_256.hexdigest())
 
result = []
for i in range(0,len(h)):
    # result.append(h[i:i+2])
    result.append(h[i])
print(result)


# print("\nSHA3-256 Hash: ", len(h))
