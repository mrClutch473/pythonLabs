cnt = 0
f=open("file.txt", 'w')
for i in range(0,12):
    temp = input()
    f.write(temp + "\n")
f.close()
f=open("file.txt", 'r')
for i in range(0,12):
    temp = int(f.readline())
    if temp%3==2:
        cnt += 1
print(cnt)