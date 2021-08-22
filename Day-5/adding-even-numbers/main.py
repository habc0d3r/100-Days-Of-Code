# using steps in range()
total = 0
for num in range(2, 101, 2):
  total += num
print(total)

# without stepping in range
total_2 = 0
for number in range(1, 101):
  if number % 2 == 0:
    total_2 += number
print(total_2)