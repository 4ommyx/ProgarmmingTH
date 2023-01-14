num = []
count = int(input(""))
for i in range (count):
    n = int(input(""))
    num.append(n)
num.sort()
print(num[0])
print(num[-1])