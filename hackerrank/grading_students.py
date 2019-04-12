def grading_students(grades):
    for i in range(0, len(grades)):
        rem = 5-(grades[i] % 5)
        if rem <= 2 and grades[i] + rem <= 100 and grades[i]+rem >= 40:
            grades[i] += rem
    return grades


grades = [73, 67, 38, 33, 100, 0, 99, 75, 44]
print(grading_students(grades))
