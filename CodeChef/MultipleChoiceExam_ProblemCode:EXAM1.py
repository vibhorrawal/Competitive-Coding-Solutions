# cook your dish here
t = int(input())
for a in range(t):
    n = int(input())
    c = str(input())
    d = str(input())
    a = [i for i in c]
    q = [j for j in d]
    p = 0 
    total = 0
    while p < n:
        if a[p]==q[p]:
            total += 1
            p += 1
        elif q[p] == 'N':
            p+=1
        else :
            p += 2
    print(total)
