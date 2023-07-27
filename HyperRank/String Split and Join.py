
def split_and_join(line):
    P = line.split(" ")
    A = "-".join(P)
    return A


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)