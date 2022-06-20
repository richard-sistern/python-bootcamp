# 78 65 89 86 55 91 64 89

student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

print(max(student_scores))