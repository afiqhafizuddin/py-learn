x , y = 3, 4
print(x , y)

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()

print(y)

x = (5, 1, 3)
y = (6, 0, 0)
z = (5, 0, 300)
zz = (0, 1000, 2000)
xx = (4, 100, 200)

print(x < y)
print(x < z)
print(x < zz)
print(x < xx)

# tmp = list()
# for k, v in c.items() :
#     tmp.append( (v, k) )

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])

# name = input("Enter file:")
# if len(name) < 1: 
#     name = "mbox-short.txt"
#     handle = open(name)
#     d = dict()

#     for line in handle:
#         if not line.startswith(("From ")):
#             continue
#         else:
#             line = line.split()
#             line = line[5]
#             line = line[0:2]
#             d[line] = d.get(line, 0) + 1

#     lst = list()
#     for value, count in d.items():
#         lst.append((value, count))

#     lst.sort()
#     for value, count in lst:
#         print(value, count)

name = input("Enter file:")
if len(name) > 1:
    name = "mbox-short.txt"

handle = open(name)
new_tuples = () # empty tuples
dict_1 = dict()

for line in handle:
    if line.startswith('From '):
        split_ = line.split()
        split1 = split_[5].split(":")
        dict_1[split1[0]] = dict_1.get(split1[0], 0) + 1
new_tuples = sorted(dict_1.items())
for k, v in new_tuples:
    print(f"{k} {v}")