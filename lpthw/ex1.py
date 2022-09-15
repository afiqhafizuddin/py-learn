print("Hello, world")
print("Hello, again")
print("I like typing this")
print("this is me having fun")
print("Yay printing")
print("i'd much rather you not")
print("i say do not touch this")


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(pos)
print(data[pos:pos+3]) # exclusive the end point

name = "Siti Nur Athiffah binti Ayub"
nickname = name.find("A")
print(name[nickname:nickname+8])



text = "X-DSPAM-Confidence:    0.8475"

text.find("0")

num = float(text[text.find("0.8475"):])
print(num)








