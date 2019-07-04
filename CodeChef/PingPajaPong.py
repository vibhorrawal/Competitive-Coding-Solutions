# cook your dish here
t = int(input())
for i in range(t):
    X, Y, K = list(map(int, input().split()))
    m = (X+Y)//K
    if(m%2==0):
        print("Chef")
    else:
        print("Paja")
