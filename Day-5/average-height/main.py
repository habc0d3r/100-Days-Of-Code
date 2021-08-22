student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# code for calculating total height #sum() function works like this
total = 0
for height in student_heights:
  total += height
# print(total)
# code for calculating no of students #len() function works like this
count_student = 0
for student in student_heights:
  count_student += 1
# print(count)
# code for finding average
avg_height = (total/count_student)
print(round(avg_height))


