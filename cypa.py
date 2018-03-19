# grid
# 7 | 8 | 9
# 4 | 5 | 6
# 1 | 2 | 3

#  Intro
name = raw_input("What is your name? \n").strip().title()
ans = raw_input("Hi Michelle! Yumana play some game? \n")



def grid9():
    print("You win I guess. There is no prize, please leave")

# def grid8():

# def grid7():

# def grid6():

def grid5():
    print("No bears")

def grid4():
    print("""It sings ever so sweetly that you fall asleep and drown.
    That's possible apparently but you might be the first person it's happened to.
    Congratulations on a...I guess, interesting death. See you in Valhalla\n""")

def grid3():
    print("Argh! Bears! You're dead! (from bears)")

def grid2():
    ans2 = raw_input("""Anneka sees a fellow adventurer and decides to come along with you
    after a final scream at the seagulls about life insurance premiums.
    You've gained a new companion! She is the worst. North? Maybe bears. I'd try East?\n """)
    if ans2 == "North":
        grid5()
    elif ans2 == "East":
        grid3()

def grid1():
    ans1 = raw_input("""You wake up in the sea, what the fuck happened there?!
    Just north of you there's a small golden ocelot hovering above the sea and
    singing a gentle lullaby about gentlemen and their ways.
    To the east, Anekka Rice begs seagulls for challenges. Which way will you go? """)
    if ans1 == "North":
        grid4()
    elif ans1 == "East":
        grid2()

if ans == "yes":
    grid1()
else:
    print("okbye i hope snakes eat you")


print("Thanks for having a play!")
