name = raw_input("What is your name? ").strip().title()

ans = raw_input("Hi Michelle! Yumana play some game? ")

def question2():
    ans2 = input("How many pigs do you take with you to change a lightbulb? ")
    if ans2 < 10:
        print("Correct! More than 10 pigs is too many pigs")
    else:
        print("Goodness me, you're positively packing that place with pigs. You're absolutely mental. You die of pig-cramping, obviously. What were you thinking?")

if ans == "yes":
    print("oo de lally")
    question2()
else:
    print("okbye i hope snakes eat you")



print("Thanks for having a play!")
