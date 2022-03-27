largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "Done":
        break
    print(num)
    try:
        num = int(num)
        if largest is None or largest < num:
            largest = num
        elif smallest is None or smallest > num:
            smallest = num
    except ValueError:
        print("Invalid input")
        continue

print('Maximum is', largest)
print('Minimum is', smallest)

