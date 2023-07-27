if __name__ == '__main__':
    report = []
    for x in range(int(input())):
        name = input()
        score = float(input())
        report.append([name, score])
    sorted_report = sorted(list(set([x[1] for x in report])))
    second_lowest = sorted_report[1]

    # second_lowest = sorted(list(set(score)))
    # for x in report:
    # if score = x[1]:
    # report.append(score)
    # second_lowest = student

    low_final = []
    for students in report:
        if second_lowest == students[1]:
            low_final.append(students[0])

    for students in low_final:
        print(students)