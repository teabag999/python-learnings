a = input("Enter the number between 1 to 10: ")
print(f"Multiplication table of {a} is: ")

for i in range(1, 11):
    print(f"{int(a)} X (i) = {int(a)*i}")
