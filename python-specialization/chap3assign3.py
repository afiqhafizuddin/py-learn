score = input("Enter Score: ")
score_float = float(score)

if score_float >= 0.9 and score_float <= 1.0:
    print("A")
elif score_float >= 0.8 and score_float < 0.9:
    print("B")
elif score_float >= 0.7 and score_float < 0.8:
    print("C")
elif score_float >= 0.6 and score_float < 0.7:
    print("D")
elif score_float < 0.6:
    print("F")
else:
    print(
        "ERROR!\n"
        "The score entered is out of range\n"
        "Please enter score between the range of 0.0 and 1.0"        
        )