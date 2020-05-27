import hashlib

final = "e246dbab7ae3a6ed41749e20518fcecd"

w = open("words.txt", "r")
for word in w.read().split():
    flag = "tjctf{"+word+"}"
    hash_obj = hashlib.md5(flag.encode())
    possible = hash_obj.hexdigest()
    if possible == final:
        print(flag)
        break
    else:
        print("No match found")

    
    
