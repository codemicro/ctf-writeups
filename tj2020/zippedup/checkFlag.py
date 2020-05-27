file = 1
for i in range(1001):
    f = open(str(file)+".txt")
    print(f.readline())
    file += 1
    f.close()
print("Finished.")
