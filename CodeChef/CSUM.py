# cook your dish here
for i in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    a=0
    b=n-1
    while(True):
        p=l[a]
        q=l[b]
        if a==b:
            print("No")
            break
        if p+q==k:
            print("Yes")
            break
        if p+q>k:
            b-=1
        if p+q<k:
            a+=1
                
