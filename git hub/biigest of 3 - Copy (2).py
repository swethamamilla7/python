def max3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
a=int(input())
b=int(input())
c=int(input())
print(max3(a,b,c))
