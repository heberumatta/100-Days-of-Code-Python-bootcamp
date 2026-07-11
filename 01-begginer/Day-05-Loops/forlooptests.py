student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total_exam_score = sum(student_scores)
print(total_exam_score)

#We can use "sum" or use the for loop:
total_exam_score = 0
for score in student_scores:
    #print(total_exam_score, "+", score)
    total_exam_score += score

print(total_exam_score)

#PAUSE 1

highest_score = student_scores[0]
lowest_score = student_scores[0]

for score in student_scores:
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score

print("The highest score with for loop is ", highest_score)
print("The lowest score with for loop is ", lowest_score,"\n")

print("The highest score with max() is ", max(student_scores))
print("The lowest score with min() is ", min(student_scores))
