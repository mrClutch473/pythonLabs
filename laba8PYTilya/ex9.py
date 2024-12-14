cnt = 1
f=open("file.txt", 'w')
for i in range(0,16):
    temp = input()
    f.write(temp + "\n")
f.close()
f=open("file.txt", 'r')
for i in range(0,16):
    temp = int(f.readline())
    if abs(temp)<2 or abs(temp)>7:
        cnt *= temp
print(cnt)