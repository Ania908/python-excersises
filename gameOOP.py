# kontynuacja do cwiczenia 43

import time

class engine(object):

    def __init__(self, first_scene):
        self.first_scene = first_scene

    def play (self):

        current_scene = self.first_scene

        while True:
            print "\n-------------"
            current_scene = current_scene.enter()

class scene(object):

    def enter(self):
        print "This scene is not ready yet."
        exit(1)

class start(scene):
    def enter(self):
        print """
        Welcome!
        In each situation you can choose
        one out of the following three:
        'yes'
        'no'
        'back'
        Just type them in whenever asked
        to answer something
        Is it clear?
        """
        odp = raw_input('> ')
        if odp == 'yes':
            print "Great! Let's begin."
            return house()
        elif odp == 'no':
            print "Ok, let's try again."
            return start()
        elif odp == 'back':
            print "There's nowhere to go back to."
            return start()
        else:
            return typo()

class house(scene):
    def enter(self):
        print "HOUSE"
        print """
        It's dark and quite cold. The skay
        gray and cloudy. You see a big, girm
        looking house in front of you. Do you
        want to go in?
        """
        odp = raw_input('> ')
        if odp == 'yes':
            return corridor()
        elif odp == 'no':
            print """
            You decide to wonder around the house
            and find a garden.
            """
            return garden()
        elif odp == 'back':
            print """
            There's nowhere to go back to.
            """
        else:
            print "I didn't get it. Let's try again."
            return house()

class corridor(scene):
    def enter(self):
        print "CORRIDOR"
        print """
        Inside the house  there's a long, dark
        corridor. Youo see closed dooron your
        right. The knob is big and made of something
        kind of dark metal. Its shape reminds you of
        an ugly face. Do you want to go in?
        """
        odp = raw_input('> ')
        if odp == 'yes':
            return room1()
        elif odp == 'no':
            print """
            You continue looking around the corridor. You
            notice another door. Its on your left, painted
            in the same clour as the walls, almost invisible
            in the dim light. o you want to go in in?
            """
            odp = raw_input('> ')
            if odp == 'yes':
                return room2()
            elif odp == 'no':
                print """
                You decide to go toward the light you can see (barely)
                at the end of the corridor. It turns out to be a back
                door leading to a garden behind the house. You go there.
                """
                return garden()
            elif odp == 'back':
                return house()
            else:
                print "I didn't get it. Let's try again."
                return corridor()
        elif odp == 'back':
            return house()
        else:
            print "I didn't get it. Let's try again."
            return corridor()

class garden(scene):
    def enter(self):
        print "GARDEN"
        print """
        You find a garden behind the house. You notice
        a bog tree in it. Do you want to examin the tree?
        """
        odp = raw_input('> ')
        if odp == 'yes':
            return tree()
        elif odp == 'no':
            print """
            You continue looking around the garden and notice a small
            graveyard right behind the garden's fence. Do you want to
            jump over the fence and go there?
            """
            odp = raw_input('> ')
            if odp == 'yes':
                return graveyard()
            elif odp == 'no':
                """
                You go back to the front of the house.
                """
                return house()
            elif odp == 'back':
                return house()
            else:
                print "I didn't get it. Let's try again."
                return garden()
        elif odp == 'back':
            return house()
        else:
            print "I didn't get it. Let's try again."
            return garden()

class room1(scene):
    def enter(self):
        print "ROOM1"
        print """
        You enter a fairly big room. There's an enormous
        painting of a man with incredibely braided hair.
        It feels like the painting is looking at you. Scary...
        You notice a book shelf in the opposite corner.
        Do you want to examin it?
        """
        odp = raw_input('> ')
        if odp == 'yes':
            print """
            Among the books you find an old piece of paper. Could
            be a map? Do you want to take it?
            """
            odp = raw_input('> ')
            if odp == 'yes':
                print"""
                It turns out to actually be a map. Lucky you! It says
                that there's a treasuere hidden around the house. According
                to the map you should look for it near a big tree in garden
                behind the house. Do you want to leave this room to start
                your search?
                """
                odp = raw_input('> ')
                if odp == 'yes':
                    return corridor()
                elif odp == 'no':
                    return room1()
                elif odp == 'back':
                    return room()
                else:
                    print "I didn't get it. Let's try again."
                    return room1()
            elif odp == 'no':
                print """
                You continue searching the room.
                """
                return trap_room1()
            elif odp == 'back':
                return trap_room1()
            else:
                print "I didn't get it. Let's try again."
                return room1()

class room2(scene):
    def enter(self):
        print "ROOM2"
        print """
        You found a room. It's scary. You notice a weird
        looking lever. Do you want to pull it?
        """
        odp = raw_input('> ')
        if odp == 'yes':
            return trap_room2()
        elif odp == 'no':
            print """
            There's nothing else to do here. Do you want to leave?
            """
            odp = raw_input('> ')
            if odp == 'yes':
                return corridor()
            elif odp == 'no':
                return room2()
            elif odp == 'back':
                return corridor()
            else:
                print "I didn't get it. Let's try again."
                return room2()
        elif odp == 'back':
            corridor()
        else:
            print "I didn't get it. Let's try again."
            return room2()

class tree(scene):
    def enter(self):
        print "TREE"
        print """
        There's what seems to be a treehouse. Do you want to climb there?
        """
        odp = raw_input('> ')
        if odp == 'yes':
            print """
            You fall down on your way up there. You die.
            """
            exit(1)
        elif odp == 'no':
            return treasure()
        elif odp == 'back':
            return garden()
        else:
            print "I didn't get it. Let's try again."
            return tree()

class graveyard(scene):
    def enter(self):
        print "GRAVEYARD"
        print """
        So... You accidentaly interrupt a vampire meeting.
        Unfortunate. Good news: you don't get killed.
        Bad news: you are one of the vampires now. Good luck!
        """
        time.sleep(3)
        exit(1)

class trap_room1(scene):
    def enter (self):
        print "TRAP"
        print """
        The weird painting keeps looking at you. Did it wink just now!?
        You look into the old mans eyes. You feel like you probably
        shouldn't, but it's so calm here. And you are so sleepy...
        """
        time.sleep(5)
        print """
        You wake up just a second too late to react. The last thing you
        see before falling down into a traphole is the man from the painting
        smiling wildly at you.
        """
        time.sleep(4)
        print """
        You died.
        """
        exit(1)

class trap_room2(scene):
    def enter(self):
        print "TRAP"
        print """
        It is a trap and you die.
        """
        exit(1)

class treasure(scene):
    def enter(self):
        print "TREASURE"
        print """
        You  look around and notice something hidden under the trees
        big root. You decide take it. It turns out to be a treasure!
        Seems like you got really rich just now. Congratulations!
        """
        time.sleep(3)
        exit(1)


a_game = engine(start())
a_game.play()
