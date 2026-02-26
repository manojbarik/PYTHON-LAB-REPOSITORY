math=int(input("enter the mark secured : "))
phy=int(input("enter the mark secured : "))
py=int(input("enter the mark secured : "))
che=int(input("enter the mark secured : "))
daa=int(input("enter the mark secured : "))
 
max=250

fullmark= math+phy+py+che+daa

per=(fullmark/max)*100

print(" the percentage secured in exam:",per)

if(per>=90 and per<=100):
    print("grade is O")
elif(per>=80 and per<=90):
    print("grade is E")
elif(per>70 and per<=80):
    print("grade is A")
elif(per>60 and per<=70):
    print("grade is B")
elif(per>50 and per<=60):
    print("grade is C")
elif(per>40 and per<=50):
    print("grade is D")

else:
    print("the candidate is fail")