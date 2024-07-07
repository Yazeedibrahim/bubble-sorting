a = [10,4,9,6,2,7,1,5,3,4]

for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j] > a[j+1]:

            a[j],a[j+1]= a[j+1],a[j]

print("sorted",a)