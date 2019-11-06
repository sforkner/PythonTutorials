import hashlib

# create a sha1 hash object
hash_object = hashlib.new("sha1", "password123".encode('utf-8'))

hashed = hash_object.hexdigest().upper()
print("\n", hashed, "\n")
