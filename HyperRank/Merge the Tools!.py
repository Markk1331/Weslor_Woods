
def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        abc = []
        for i in string[i:i+k]:
            if i not in abc:
                abc.append(i)
        print(('').join(abc))




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)