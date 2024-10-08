from decimal import Decimal as a

input_data = open("input.txt","r")
data = input_data.read()
d = int(data)
E = 2.7182818284590452353602875
b = a(E)
g = list(str(b))
for g in range(0,d):
    print(g)




