
import math

n = input("")
leng = n.split() # แยกแต่ str
# print(leng)
for i in range(len(leng)):
    leng[i] = float(leng[i])

# leng = int(leng)
# print(leng)

ans = math.sqrt(leng[0]**2 + leng[1]**2)
print("%.6f" %ans)