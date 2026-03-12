# wap to print even length words in a string.
s=input("enter a string: ")
y=""
for c in s:
    if c!=" ":
        y=y+c
    else:
        if len(y)%2==0:
            print(y)
        y=""
if len(y)%2==0:
    print(y)