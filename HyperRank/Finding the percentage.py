if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for x in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    grade = []
    for key, value in student_marks.items():
        if key == query_name:
            grade.append(value)

    total = 0
    for u in grade:
        total = total + sum(u)


    average = total / 3
    print("{:.2f}".format(average))