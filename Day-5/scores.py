student_scores = [180,124,165,173,189,169,146]

total_exam_score = sum(student_scores)
print(total_exam_score)

sum = 0 
for score in student_scores:
    sum+=score
print(sum)

print(max(student_scores))
maxScore = 0
for score in student_scores:
    if score>maxScore:
        maxScore=score
print(maxScore)
