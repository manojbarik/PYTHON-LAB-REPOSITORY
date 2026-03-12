# wap to find the factorial of a number.
x=int(input("enter a number: "))
f=1
if x<0:
    print("it is a negative number  and factorial is not possible")
elif x==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,x+1):
        f=f*i
    print("the factorial of %d is %d" % (x,f))
    