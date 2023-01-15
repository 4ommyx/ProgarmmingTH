st = input("")
data = st.split()
# print(data)

for i in range(len(data)):
    data[i] = int(data[i])
    x1 = data[0]
    s = data[1]
    if (x1>=-1000 and not x1<=1000) and (s>=-1000 and not s<=1000):
        break


# print(x1)
# print(s)

x2 = ((2*s)-x1)
print(x2)
