cnt = 0
f=open("file.txt", 'w')
for i in range(0,14):
    temp = input()
    f.write(temp + "\n")
f.close()
f=open("file.txt", 'r')
for i in range(0,14):
    temp = int(f.readline())
    if temp<0:
        cnt += abs(temp)
print(cnt)