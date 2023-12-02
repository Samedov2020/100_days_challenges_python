# You are going to write a program that calculates the highest score from a List of scores.

student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

length=len(student_scores)-1
for i in range(length):
    if student_scores[i]>student_scores[i+1]:
        student_scores[i],student_scores[i+1]=student_scores[i+1],student_scores[i]
print(f"The highest score in the class is: {student_scores[-1]}")