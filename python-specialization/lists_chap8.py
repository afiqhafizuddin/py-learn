x = list(range(5))
print(x)

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))

fruit = "Banana"
# fruit[0] = "b" 
print(fruit)

#fname = input("Enter file name: ")
file = open(romeo.txt) #open the file
dictionary = list() # assigning an empty "dictionary" list
for line in file:
    words = line.split()
    for word in words:
        if word not in dictionary:
            dictionary.append(word)
        elif word in dictionary:
            continue
dictionary.sort()
print(dictionary)


# answer
fname = input("Enter file name: ")
fh = open(fname)
dictionary = list()
for line in fh:
    line = line.rstrip()
    line = line.split()
    for word in line: 
        if word not in dictionary:
            dictionary.append(word)
            
dictionary.sort()
print(dictionary)