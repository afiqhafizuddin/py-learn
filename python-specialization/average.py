count = 0
sum = 0
list = [9,41, 12, 2, 3, 85, 69, 45, 25, 54, 45]
print("Before", count, sum)
for value in list:
    count += 1
    sum = sum + value
    print(count, sum, value)
print("After", count, sum, sum/count)

print("\n")

found = False
print("Before", found)
for value in list:
    if value == 2:
        found = True
    else:
        found = False
    print(found, value)
print("After", found)

print("\n")

largest = 0 
print("Before", largest)
for number in list:
    if number > largest:
        largest = number
    print(largest, number)
print("After", largest)

print("\n")

smallest = None
print("Before", smallest)
for number in list:
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    print(smallest, number)
print("After", smallest)

