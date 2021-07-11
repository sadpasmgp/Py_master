

def pearl_room():
    print("This room has pearls. How much do you take?")

    choice = int(input(" Enter any number> "))
    if choice < 100:
        print("You are not greedy")
    else:
        print("You are very greedy")


def bear_room():
    print(""" There is a hungry bear here in this room.
    You must be cautious!""")
    print("Feed the bear to escape!")


    while True:
        choice = input("Will you feed the bear> yes or no > ")

        if choice == 'yes':
            print("You may enter pearl_room now: ")
            pearl_room()
        elif choice == 'no':
            print("Your funeral. You are eaten by hungry bear:")
            break

def start():
    print("You are entering pearl castle with hungry bear")
    print("Do you like to enter?")

    choice = input("yes or no?> ")

    if choice == 'yes':
        bear_room()
    else:
        print("You saved your life by not entering the castle")

start()
