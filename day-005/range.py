# range(start, end, step)
for number in range(1, 10): # 1..(n - 1)
    print(number)

for number in range(1, 10, 3): 
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)