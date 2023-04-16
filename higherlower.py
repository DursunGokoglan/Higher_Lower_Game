import random
from gamedata import data

print("Welcome to HigherLower! You will guess which one has more followers on Instagram.")

found = True
score = 0

a = data[random.randint(0, len(data) - 1)]
data.remove(a)

while found:

    b = data[random.randint(0, len(data) - 1)]
    data.remove(b)

    f_a = a['follower_count']
    f_b = b['follower_count']
    
    if f_a > f_b:
        answer = "A"
    else:
        answer = "B"

    print(f"Psst! The answer is {answer}")

    print(f"Your score is {score}")
    print(f"A is {a['name']}, a {a['description']} from {a['country']}.")
    print(f"B is {b['name']}, a {b['description']} from {b['country']}.")
    
    pick = input("Do you choose A or B?: ")

    if pick == answer:
        score += 1
        a = b

    else:
        found = False
        print(f"Your final score is {score}")