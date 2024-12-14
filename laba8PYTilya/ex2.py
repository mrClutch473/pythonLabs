cnt = 1
f=open("file.txt", 'w')
for i in range(0,15):
    temp = input()
    f.write(temp + "\n")
f.close()
f=open("file.txt", 'r')
for i in range(0,15):
    temp = int(f.readline())
    if temp**2<16:
        cnt *= temp
print(cnt)