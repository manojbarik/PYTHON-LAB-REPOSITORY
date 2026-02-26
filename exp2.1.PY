p=int(input("Enter the value of p : "))
t=int(input("Enter the value of t: "))
r=float(input("Enter the value of r: "))
si=(p*t**r)/100
print("simple intrest is:",si);
ci=p*((1+r/100)**t)
print("the compound intrest is:",ci);