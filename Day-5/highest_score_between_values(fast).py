student_scores=input("input your numbers").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])

max_score=0
for score in student_scores:
    if score > max_score:
        max_score=score

print(max_score)