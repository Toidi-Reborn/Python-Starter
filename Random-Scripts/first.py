
class Program():
    def __init__(self, *args, **kwargs):
	    self.lang = input("what Language: ")
	    self.version = float(input("Version?: "))
	    self.skill = input("What skill level?: ")

    def upgrade(self):
        new_version = float(input("What new verison?: "))
        print("it has been updated", self.lang)
        self.version = new_version

p1 = Program()
#p2 = Program()















