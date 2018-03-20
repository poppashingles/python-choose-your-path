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
    ans5 = raw_input("""You take a look west. It's that ocelot again, singing away. He might have sweets in his pockets...
    To your directly east, it couldn't be more easterly, John McCaine waits on a small island to show you how high he can't lift his arms.
    It's a bit sad, someone has put a silly hat on him and he can't take it off.
    Lastly you could head to the North. It's a distance away but you're pretty sure you can make out a small boat.
    It looks deserted, but in stories deserted things usually aren't because otherwise they wouldn't be there.
    Narratively speaking it's just pointless. Honestly though it could go either way, I've not written it yet.
    Which way draws your fancy? West to Sweets, East to McCaine or North to a possibly not deserted small boat? """)
    if ans5.upper() == "WEST":
        grid4()
    elif ans5.upper() == "EAST":
        grid6()
    elif ans5.upper() == "NORTH":
        grid8()

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
    if ans2.upper() == "NORTH":
        grid5()
    elif ans2.upper() == "EAST":
        grid3()

def grid1():
    ans1 = raw_input("""You wake up in the sea, what the fuck happened there?!
    Just north of you there's a small golden ocelot hovering above the sea and
    singing a gentle lullaby about gentlemen and their ways.
    To the east, Anekka Rice begs seagulls for challenges. Which way will you go? """)
    if ans1.upper() == "NORTH":
        grid4()
    elif ans1.upper() == "EAST":
        grid2()

if ans.upper() == "YES":
    grid1()
else:
    print("okbye i hope snakes eat you")


print("Thanks for having a play!")
