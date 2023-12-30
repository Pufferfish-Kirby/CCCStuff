drops = int(input())
x = []
y = []
for _ in range(drops):
    a, b = map(int, input().split(","))
    x.append(a)
    y.append(b)
x.sort(); y.sort()
print(-1+x[0],-1+y[0], sep=",")
print(1+x[(len(x)-1)],1+y[(len(y)-1)], sep=",")
