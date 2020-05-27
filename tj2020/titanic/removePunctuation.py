import string

w = open('nopunct.txt', 'w')
foundWords = []

f = open('script.txt', 'r')
for i in f:
    s = i.replace('.','')
    w.write(s)

print("Finished.")
    
