# cook your dish here
for t in range(int(input())):
    l,r=map(int,input().split())
    n=r-l+1
    if n == 0:
        exit()
    if(n%4==0):
        print('Even')
    elif(n%4==2):
        print('Odd')
    elif(n%4==1):
        if(l%2==1):
            print('Odd')
        else:
            print('Even')
    else:
        if(l%2==0):
            print('Odd')
        else:
            print('Even')        
