marks = [12, 56, 32, 98, 3, 15, 12]

index = 0
for mark in marks:
    print(mark)
    if index == 3:
        print("Aadesh, test!")
    index += 1

for index, mark in enumerate(marks, start=1):
    print(mark)
    if index == 5:
        print("Aadesh, test!")
