a = 0
b = 1
even_sum = 0

print("Fibonacci series up to 1000:")

while a <= 1000:
    print(a, end=" ")
    
    if a % 2 == 0:
        even_sum += a
    
    a, b = b, a + b

print("\nSum of even-valued terms:", even_sum)