if __name__ == '__main__':
    B = {}
    for x in range(int(input())):
        name = input()
        score = float(input())
        B[name] = score

    mylist = list(B.values())
    second_last = sorted(list(set(mylist)))[1]

    grade = []
    for key, value in B.items():
        if value == second_last:
            grade.append(key)
    grade.sort()

    for students in grade:
        print(students)