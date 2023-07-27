def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)):
        if string[i:].startswith(sub_string):
            count = count + 1
    return count

if __name__ == '__main__':
    n = input()
    sub_n = input()
    n.strip()
    sub_n.strip()
    count = count_substring(n, sub_n)
    print(count)