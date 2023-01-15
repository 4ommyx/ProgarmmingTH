n = input("")
num = n.split()

mes = input("")

for i in range(len(num)):
    num[i] = int(num[i])
# print(mes)
num.sort()
#print(num)

for j in range(len(mes)):
    if mes[j] == "A":
        print(num[0],end=" ")
    elif mes[j] == "B":
        print(num[1],end=" ")
    elif mes[j] == "C":
        print(num[-1],end=" ")