C = 0 
H = 0
O = 0

with open('task2input.txt', 'r') as input:
    C, H, O = input.readlines()

a = []
a.append(int(C) // 2)
a.append(int(H) // 6)
a.append(int(O))

with open('task2output.txt', 'w') as ouput:
    ouput.write(str(min(a)))

