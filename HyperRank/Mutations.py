def mutate_string(string, position, character):
    A = list(string)
    A[position] = character
    I = "".join(A)
    return I

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)