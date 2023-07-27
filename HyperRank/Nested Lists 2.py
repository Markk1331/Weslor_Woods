if __name__ == '__main__':
    score_list = []
    record = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record[name] = score
    record = sorted(record.items(),key=lambda x:x[1], reverse=True)
    print(record[-1][0])
    print(record[-2][0])