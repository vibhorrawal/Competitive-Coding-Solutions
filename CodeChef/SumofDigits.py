# cook your dish here
t = int(input())
for i in range(t):
    a = str(input())
    s = [int(b) for b in a]
    print(sum(s))
