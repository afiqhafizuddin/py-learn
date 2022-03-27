parse = dict()
parse['mango'] = "RM10"
parse['rambutan'] = "RM15"
parse['durian'] = "RM150"

print(parse)

# counting with ditionary
ccc = dict()
ccc['csev'] = 1
ccc['zhen'] = 1
ccc['marquard'] = 1

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen', 'csev', 'zqian']
for name in names: # iterate thru the elements in the list
    if name not in counts: # inserting the list elements into the dictionary
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)

# count words in line of text
  

# quiz

stuff = dict()
print(stuff.get('candy', -1))






