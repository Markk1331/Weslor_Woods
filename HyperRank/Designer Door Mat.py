k,w = map(int,input().split())
for i in range(1,k,2):
    print((i* ".|.").center(w,"-"))
print("WELCOME".center(w,"-"))
for x in range(k-2,-1,-2):
    print((x*".|.").center(w,"-"))