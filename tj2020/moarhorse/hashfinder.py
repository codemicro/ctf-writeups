import hashlib

print("Loading wordlist...")
wordlist = open("rockyou.txt", encoding="utf8", errors="ignore").read().split("\n")

boss_speed = int(hashlib.md5(("Horse_MechaOmkar-YG6BPRJM").encode()).hexdigest(), 16)
prefix = "Horse_"

print("Running")
for word in wordlist:
  if int(hashlib.md5((prefix + word).encode()).hexdigest(), 16) > boss_speed:
    print(prefix, "'" + word + "'")
print("Done")