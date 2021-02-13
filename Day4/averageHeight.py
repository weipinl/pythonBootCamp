student_heights = input("Input a list of student heights ").split()
totalHeight = 0
count = 0

for measurement in student_heights:
    totalHeight += int(measurement)
    count += 1

averageHeight = totalHeight/count

print(round(averageHeight))