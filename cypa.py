# grid
# 7 | 8 | 9
# 4 | 5 | 6
# 1 | 2 | 3


# Global variables for win conditions
bottle = False
shotgun = False


# To check if grid squares have been visited already in order to change messages
# if they are visited a second time
grid1Visited = False
grid2Visited = False
grid3Visited = False
grid4Visited = False
grid5Visited = False
grid6Visited = False
grid7Visited = False
grid8Visited = False
grid9Visited = False


#  Grid content
def grid9():
    grid9Visited = True

    if bottle == True and shotgun == False:
        ans9 = raw_input("""You finally, after literally minutes of this adventure, meet the wizard that John McCaine mentioned back in grid 6.
        It looks more like a tired old man with a scraggly beard than a wizard though.
        Well, you have that broken bottle. Stab him with it?\n """)
        if ans9.upper() == "YES":
            print("""You've murdered a lost old man. Nice work. Why would he be a wizard?!
            You had zero evidence of that.\n """)
        elif ans9.upper() == "NO":
            print("Well...yeah, obviously. Why would you murder an old man based on the word of a clearly insane John McCaine? You win!")

    elif bottle == False and shotgun == True:
        ans9 = raw_input("""You come across an old man (not like that) standing on a small island with a little coconut tree.
        Well, you have that shotgun from the HMS Sugababes Past. Shoot him with it?\n """)
        if ans9.upper() == "YES":
            print("""You've murdered a lost old man. Nice work....just....based on what?! Why would you do that?!\n """)
        elif ans9.upper() == "NO":
            print("Well...yeah, obviously. Why would you murder an old man? You win!")

    elif bottle == True and shotgun == True:
        ans9 = raw_input("""You finally, after literally minutes of this adventure, meet the wizard that John McCaine mentioned back in grid 6.
        It looks more like a tired old man with a scraggly beard than a wizard though.
        Well, you have that broken bottle. Stab him with it?\n """)
        if ans9.upper() == "YES":
            print("""You've murdered a lost old man. Nice work....just....based on what?! Why would you do that?!\n """)
        elif ans9.upper() == "NO":
            ans9b = raw_input("""Good choice, it'd be much more fun to shoot him with that shotgun you picked up from the
            Ship of the Damned Sugababes. Is that your thinking?\n """)
            if ans9.upper() == "YES":
                print("""You've murdered a lost old man. Nice work. Why would he be a wizard?!
                You had zero evidence of that.\n """)
            elif ans9.upper() == "NO":
                print("Well...yeah, obviously. Why would you murder an old man based on the word of a clearly insane John McCaine? You win!\n ")

    else:
        ans9 = raw_input("""You meet an old dude, he's just kind of standing there...
        Just leave? I guess? South or West are the only options here...\n """)
        if ans9.upper() == "WEST":
            grid8()
        elif ans9.upper() == "SOUTH":
            grid6()


def grid8():
    grid8Visited = True
    ans8 = raw_input("""You draw closer to the boat, it's super spooky and gets super spookier the closer you get.
    Might be worth sending Anneka on ahead, she's been singing showtunes and "cleaning" herself like a cat all the way here.
    What do you reckon?\n """)

    if ans8.upper() == "YES":
        print("""You pretend you need to tie your shoelace, which is tricky in the sea and you almost drown in commitment to the lie.
        She swims on ahead while you carry on not-quite-drowning. As you break the surface,
        lungs having achieved a 55% water content and decide that's been long enough, you begin to swim after Anneka who's moved on to a
        Bugsy Malone medley. Then she's harpooned. It's a bit sudden, that's harpooning for you. Then you get harpooned, obviously,
        you weren't far away from a mad woman singing 'We could have been anything that we wanted to be' suuuuuper loudly.\n""")
    elif ans8.upper() == "NO":
        ans8b = raw_input("""Probably wise, you set her a challenge of drinking the sea to keep her quiet and start to approach
        the boat stealthily. You start to climb a ladder at the back and peer over the side, seeing three faces that you recognise...
        Siobhan Donaghy, Mutya Buena and Keisha Buchanan sit on the deck in the sun, each of them readily armed but they don't notice you.
        You'd spent years wondering what happened to all of the former sugababes, so that's one mystery solved at least.
        Anyway, there's a gun within your reach, so if you want to have a go at retiring them permanently, go for it. I'm not sure
        why you would, but it's been an unusual Saint Lidwina's Day overall so sod it. Fight or run?\n """)

        global shotgun
        shotgun = True

        if ans8b.upper() == "FIGHT":
            print("""They've spent their years on the sea living well, pirating from the wealthy. Your skills are no match for theirs
            and though you wing Keisha you go down quickly. Too late you learn the lesson not to fight a pirate
            former sugababe on her own turf.\n""")
        elif ans8b.upper() == "RUN":
            print("Probably wise. You head off East, past Anneka's bloated corpse. Can't fault her commitment to a challenge.")
            grid9()


def grid7():
    grid7Visited = True

    print("You fell off the edge, that was silly. You big silly goose. Also on the way down you're eaten by geese.\n")


def grid6():
    grid6Visited = True

    ans6 = raw_input("""Bless his little cotton socks, it's a big pointy hat that says 'Oh I'm just the smelliest'.
    Help him take it off or just laugh at his plight? Nobody will judge you, it's fine. Help or laugh?\n """)

    if ans6.upper() == "HELP":
        print("""You climb up onto the island and take the hat off of his head.
        He looks you in the eye and says 'thank you for your help young'un' and presents you an item wrapped in cloth.
        'Take this, it is a weapon of legend that will help you defeat the wizard who controls these lands'
        You have acquired 'Broken bottle!' You swim off to the north\n """)
        global bottle
        bottle = True
        grid9()
    elif ans6.upper() == "LAUGH":
        print("""He looks sad, which makes it funnier.
        You swim off to the north, still giggling away. You sicken me\n """)
        grid9()


def grid5():
    grid5Visited = True

    ans5 = raw_input("""Hooray! A lack of bears. But you are in the sea (remember? it said earlier). That's not where bears live.
    You curse your damn fool self and take a look about.
    You take a look west. It's that ocelot again, singing away. He might have sweets in his pockets...
    To your directly east, it couldn't be more easterly, John McCaine waits on a small island to show you how high he can't lift his arms.
    It's a bit sad, someone has put a silly hat on him and he can't take it off.
    Lastly you could head to the North. It's a distance away but you're pretty sure you can make out a small boat.
    It looks deserted, but in stories deserted things usually aren't because otherwise they wouldn't be there.
    Narratively speaking it's just pointless. Honestly though it could go either way, I've not written it yet.
    Which way draws your fancy? West to Sweets, East to McCaine or North to a possibly not deserted small boat?\n """)

    if ans5.upper() == "WEST":
        grid4()
    elif ans5.upper() == "EAST":
        grid6()
    elif ans5.upper() == "NORTH":
        grid8()


def grid4():
    grid4Visited = True

    print("""It sings ever so sweetly that you fall asleep and drown.
    That's possible apparently but you might be the first person it's happened to.
    Congratulations on a...I guess, interesting death. See you in Valhalla\n""")


def grid3():
    grid3Visited = True

    print("Argh! Bears! You're dead! (from bears)\n")


def grid2():
    grid2Visited = True

    ans2 = raw_input("""Anneka sees a fellow adventurer and decides to come along with you
    after a final scream at the seagulls about life insurance premiums.
    You've gained a new companion! She is the worst. North? Maybe bears. I'd try East?\n """)

    if ans2.upper() == "NORTH":
        grid5()
    elif ans2.upper() == "EAST":
        grid3()


def grid1():
    grid1Visited = True

    ans1 = raw_input("""You wake up in the sea, what the fuck happened there?!
    Just north of you there's a small golden ocelot hovering above the sea and
    singing a gentle lullaby about gentlemen and their ways.
    To the east, Anekka Rice begs seagulls for challenges. Which way will you go?\n """)

    if ans1.upper() == "NORTH":
        grid4()
    elif ans1.upper() == "EAST":
        grid2()


#  Intro
name = raw_input("What is your name? \n").strip().title()
ans = raw_input("Hi Michelle! Yumana play some game? \n")

if ans.upper() == "YES":
    grid1()
else:
    print("okbye i hope snakes eat you\n")


print("Thanks for having a play!\n")
