#Simple class

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you","Hello Mister How do you do"])

bulls_on_parade = Song(["They rally around the family","With pockets full"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
