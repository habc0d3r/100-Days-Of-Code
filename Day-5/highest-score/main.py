student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

heighest = 0
for score in student_scores:
  if score > heighest:
    heighest = score
print(f"The heighest score in the class is: {heighest}")
  



