import re
x = 'From: using the : character'
y = re.findall('^F.+:', x )
print(y)

xy = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
yx = re.findall('\S+?@\S+', xy)
print(yx)

# Extracting data with ReGex
file_open = open("./regex_sum_1462268.txt")
x = list()
for line in file_open:
    y = re.findall('[0-9]+', line)
    x = x + y

total = 0
for z in x:
    total += int(z)

print(total)