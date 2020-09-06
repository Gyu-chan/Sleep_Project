a=[1,2,3,4,5,4,6,7,8,9,]
b=[6,7,8,9,10]
x=len(a)
y=len(b)

def a(n):
    count=0
    for i in range(0,5):
        count=n+i
        print(n,i,count)
    return count

print(a(x))
print(a(y))


