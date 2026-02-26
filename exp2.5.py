student={
    "Name":"Manoj Barik",
    "rollno":213,
    "course":"B.TECH",
    "city":"balasore"
}
print("element of the dictionary data:")
print(student)

print("\nkeys in dictionary:")
print(student.keys())

print("\nvalues in dictionary:")
print(student.values())

print("\nkey-values pairs:")
for key,value in student.items():
    print(key,":",value)