# cook your dish here
n = int(input())
a= l = []
a = list(range(1,n+1))
l = list(map(int,input().split()))
for i in range(n):
    b = []
    for j in range(n):
        b.append(l[j]+a[j])
    c = a.pop(0)
    a.append(c)
    print(max(b),end=" ")
    
