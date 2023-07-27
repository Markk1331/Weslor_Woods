from collections import namedtuple
s = int(input())
subjects = input().split()
total = 0
for i in range(s):
    students = namedtuple('students',subjects)
    subjects1, subjects2, subjects3, subjects4 = input().split()
    students = students(subjects1, subjects2, subjects3, subjects4)
    total += int(students.MARKS)
print(total/s)