a = [10,80,92,85,48,76,23,19,84]
for b in  range(len(a)):
    for j in range(len(a)-1-b):
        if a[j] < a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
        print(a)
