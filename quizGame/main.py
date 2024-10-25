import time
questions = ("Q1. What is the most abundant gas in Earth's atmosphere?",
             "Q2. What have chickens evolved from? ",
             "Q3. What is 9 + 10? ",
             "Q4. How many elements are in the periodic table?")
answers = ("A", "C", "E", "C")
options = ("A", "B", "C", "D", "E")
choices = (("Nitrogen", "Oxygen", "Carbon Dioxide", "Argon", "Hydrogen"),
           ("Brontosaurus", "Pterodactyl", "T-Rex", "Ankylosaurus", "Raptor"),
           ("17", "18", "19", "20", "21"),
           ("116", "117", "118", "119", "120"))
reply = []
print("----------------START--------------------")
for i in range(4):
    print("------------------------------------")
    print(questions[i])
    for x in range(5):
        print(f"{options[x]} {choices[i][x]}")
    guess = input("Enter (A, B, C, D, E): ")
    reply.append(guess)
print("----------------END--------------------")
score = 0
for i in range(4):
    if reply[i] == answers[i]:
        score += 1
print(f"You scored {score}/{len(questions)}")
if score < 3:
    print("Did you really try?\nPunishment:")
    for i in reversed(range(1, 6)):
        print(i)
        time.sleep(1)
    print("BOOM! *bomb explodes*")
else:
    print("This is an acceptable score")
for i in reversed(range(1, 6)):
    print(f"Program will end in {i}")
    time.sleep(1)
print("PROGRAM END")
