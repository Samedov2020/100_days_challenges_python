student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# TODO-1: Create an empty dictionary called student_grades.
for i in student_scores:
    if student_scores[i]<=70:
        student_scores[i]="Fail"
    elif 71<=student_scores[i]<=80:
        student_scores[i]="Acceptable"
    elif 81<=student_scores[i]<=90:
        student_scores[i]="Exceeds Expectations"
    elif 91<=student_scores[i]<=100:
        student_scores[i]="Outstanding"
print(student_scores)
        





