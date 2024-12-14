cnt = 0
f=open("file.txt", 'w')
for i in range(0,11):
    temp = input()
    f.write(temp + "\n")
f.close()
f=open("file.txt", 'r')
for i in range(0,11):
    temp = int(f.readline())
    if temp**2>25:
        cnt += 1
print(cnt)