# wap to check wheather the string is symmetrical or palindrome.


# s=input("enter a string: ")
# if s==s[::-1]:
#     print("the string is palindrome")
# else:
#     print("the string is not palindrome")



x=input("enter a string: ")
z=(str(str(x[::-1])))
if x==z:
    print("the string is palindrome")
else:
    print("the string is not palindrome")