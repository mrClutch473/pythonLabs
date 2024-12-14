cnt = 0
n = 0
f=open("file.txt", 'w')
for i in range(0,14):
    temp = input()
    f.write(temp + "\n")
f.close()
f=open("file.txt", 'r')
for i in range(0,14):
    temp = int(f.readline())
    if temp%4==1 or temp%4==3:
        cnt += temp
        n += 1
srArif = cnt/n
print(srArif)