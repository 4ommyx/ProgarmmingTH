minV,maxV = 2000000000,-2000000000

def minC(n): 
    global minV
    if n < minV:
        minV = n
    if i == count-1:
        print(minV)

def maxC(n): 
    global maxV
    if n > maxV:
        maxV = n
    if i == count-1:
        print(maxV)

count = int(input(""))
for i in range(count):
    num = int(input(""))
    minC(num)
    maxC(num)

# print(minn(num))
# print(maxx(num))

