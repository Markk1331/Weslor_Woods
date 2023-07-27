
def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        a = []
        for x in string[i:i+k]:
            if x in a:
                continue
            a.append(x)
        print(('').join(a))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)