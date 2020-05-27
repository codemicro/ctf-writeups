def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line
w = open("words.txt", "w")
found = []

with open("nopunct.txt") as f_in:
    for line in nonblank_lines(f_in):
        for word in line.split():
           s = word.lower()
           if s in found:
               print("Already in")
           else:
               print("Not in")
               found.append(s)

f_in.close()

print("\n\n")
for i in found:
    print(i)
    w.write(i)
    w.write(" ")
print("Done.")
w.close()
