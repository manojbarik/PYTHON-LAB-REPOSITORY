a = int(input("enter the value : "))

if a <= 1:
    print("not a prime number")
else:
    i = 2
    prime = True
    while i < a:       
        if a % i == 0:
            prime = False
            break
        i += 1         

    if prime:
        print(a, "is a prime number")
    else:
        print(a, "is not a prime number")
