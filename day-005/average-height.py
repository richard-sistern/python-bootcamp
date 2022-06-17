# 156 178 165 171 187
# 180 124 165 173 189 169 146

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Proper way
print(round(sum(student_heights) / len(student_heights)))

# Loopy way
loop_counter = 0
total_height = 0

for height in student_heights:
    loop_counter += 1
    total_height += height 

print(round(total_height / loop_counter))
