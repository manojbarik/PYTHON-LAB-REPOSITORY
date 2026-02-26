numbers = []
n = int(input("Enter how many numbers you want to input: "))
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
unique_numbers = list(set(numbers))
unique_numbers.sort()
print("Original list:", numbers)
print("List after removing duplicates and sorting:", unique_numbers)
