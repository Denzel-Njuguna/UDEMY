student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={
    
}
len_of_dict = len(student_scores)
for each in student_scores:
    grade = int(student_scores[each])
    if 91 <= grade <=100:
        student_grades[each] = "Outstanding"
    elif 81<= grade<=90:
        student_grades[each] = "Exceeds Expectations"
    elif 71<= grade <= 80:
        student_grades[each] = "Acceptable"
    else:
        student_grades[each] = "Fail"
print(student_grades)