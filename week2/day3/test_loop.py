import random

arr=[]
for i in range(0, 15):
    numbers = random.randint(1, 10)
    arr.append(numbers)

for i in arr:
    if i%2 == 0:
        continue
    print("{}은 짝수".format(i))