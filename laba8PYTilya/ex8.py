cnt = 1
f=open("file.txt", 'w')
for i in range(0,13):
    temp = input()
    f.write(temp + "\n")
f.close()
f=open("file.txt", 'r')
for i in range(0,13):
    temp = int(f.readline())
    if abs(temp)>=1 and abs(temp)<=5:
        cnt *= temp
print(cnt)