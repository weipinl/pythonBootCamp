student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
maxNum = 0 

for score in student_scores:
    currentScore = score 
    if currentScore > maxNum:
        maxNum = currentScore
    else:
        continue

print(maxNum)