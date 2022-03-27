print("hello, world")
def getUsername(name):
    if len(name) > 15:
        return("Invalid username. Try again")
    elif len(name) < 5:
        return("Invalid username. Try again")
    else:
        return("Valid username")

print (getUsername("Afiq Hafizuddin bin Zainal"))


