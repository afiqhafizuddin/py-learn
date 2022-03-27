# TODO: kjsncsnnsnscnsdjn
def getName(name):
    print(str(name))
    if len(name) > 15:
        print("Invalid Username")
    elif len(name) < 3:
        print("Invalid Username")
    else:
        print("Valid Username")

getName("Afiq Hafizuddin")

print('afiq hafizuddin bin zainal')

def counter(start, stop):
    x = start
    if start > stop:
        returnString = "Counting down: "
        while x >= stop:
            returnString += str(x)
            x = x-1
            if start != stop:
                returnString += ","
    else:
        returnString = "Counting up: "
        while x <= stop:
            returnString += str(x)
            x = x + 1
            if start != stop:
                returnString += ","
    return returnString

print(counter(1, 10))
print(counter(2, 1))
print(counter(5,5))


def even_numbers(maximum):
    return_string = ""
    for x in range(0, maximum + 1):
        if x != 0 and x % 2 == 0:
            return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10))  # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

def getName(name):
    print(name)
    if len(name) > 15 and len(name) < 3:
        print("Invalid Username")
    else:
        print("Valid USername")

getName("Afiq Hafizuddin Bin Zainal")

