fname = input("Enter file name: ")
if len(fname) > 1:
    fname = "mbox-short.txt"

file = open(fname)
count = 0
for line in file:
    words = line.split()
    if len(words) > 2 and words[0] == "From":
        print(words[1])
        count += 1
    else:
        continue

print('There were' + count + 'lines in the file with From as the first word')