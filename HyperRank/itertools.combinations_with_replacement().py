from itertools import combinations_with_replacement
N,M = input().split(" ")
print(*list(map("".join,combinations_with_replacement(sorted(str(N).upper()),int(M)))), sep = '\n')
