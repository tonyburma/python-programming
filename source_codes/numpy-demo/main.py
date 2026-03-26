import numpy as np

# Rows = students, Columns = subjects
marks = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [90, 91, 85],
    [60, 65, 70],
    [95, 89, 93]
])

# 1. Average score per student
student_avg = np.mean(marks, axis=1)

# 2. Average score per subject
subject_avg = np.mean(marks, axis=0)

# 3. Find top scorer (based on total marks)
total_scores = np.sum(marks, axis=1)
top_student_index = np.argmax(total_scores)

print("Student Averages:", student_avg)
print("Subject Averages:", subject_avg)
print("Top Student Index:", top_student_index)