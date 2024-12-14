cnt = 0
f=open("file.txt", 'w')
for i in range(0,14):
    temp = input()
    f.write(temp + "\n")
f.close()
f=open("file.txt", 'r')
for i in range(0,14):
    temp = int(f.readline())
    if i!=0 and temp%i==0:
        cnt += 1
print(cnt)