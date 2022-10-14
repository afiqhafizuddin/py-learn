print("Hello, world")
def uew(name):
    print("Hi, My name is " + str(name))
uew("Kay")
def areaTriangle(height, base):
    return height * base / 2
area_A = areaTriangle(9,9)
area_B = areaTriangle(10,10)
total_area = area_B + area_A
print(total_area)
def greetings(name):
    print("Hello, world")
    print("Welcome " + str(name))
greetings("Ahmad")

def getUsername(name):
    if len(name) > 15:
        return"Invalid username. Try again"
    elif len(name) < 5:
        return"Invalid username. Try again"
    else:
        return"Valid username"

print(getUsername("Afiq Hafizuddin bin Zainal"))

print("afiq hafizuddin bin zainal")

