# Write your code here :-)
# dog parameters


class Dog:
    """A simple attempt to model a dog."""

    # initaialization function
    def __init__(self, name):
        # default dog parameters for my class.
        self.num_legs = 4
        self.weight = 30
        self.color = "brown"
        self.breed = "lab"
        self.name = name

    ### WANT FUNCTIONS TO BE SELF CONTAINED AND NOT CALL ON ABOVE PARAMETERS SO THAT YOU CAN EASILY REUSE FUNCTIONS IN OTHER CODE
    ### SEE BELOW, CREATE BRD INSTEAD ON CALLING ON ABOVE BREED PARAMETER
    def fetch(self, item):
        if (self.breed == "lab") or (self.breed == "spaniel"):
            return item
        else:
            return "nothing"

    def bark(self, item):  # dont have to have self here but good practice to always put it
        if item == "squirrel":
            time_barked = 3  # (min)
        elif item == "human":
            time_barked = 1
        elif item == "mailman":
            time_barked = 4
        else:
            time_barked = 0

    def poop(self, food):
        if (self.breed == "lab") and (food == "chocolate"):
            bagged_poop = 2  # (lbs)
        elif (self.breed == "spaniel") and (food == "raw chicken"):
            bagged_poop = 1.5
        elif (self.breed == "terrier") and (food == "steak"):
            bagged_poop = 0.5
        else:
            bagged_poop = 0.0
        return bagged_poop

    def run(self, t_run):
        if self.breed == "lab":
            distance = t_run * (5)  # 5 meters per second
        elif self.breed == "blood hound":
            distance = t_run * (0)
        elif self.breed == "chihuahua":
            distance = t_run * (0.002)
        else:
            distance = 0
        return distance


    def sleep(self):
        ###SINCE USING TWO IF STATEMENTS, NOT AN ELIF, NEED TO SET SNORE TO FALSE FIRST SO THAT IF BOTH IF STATEMENTS DONT RUN, PROGRAM WILL STILL HAVE SNORE DEFINED
        snore = False
        if self.breed == "lab":
            snore = True
        if self.breed == "spaniel":
            snore = True
        return snore


print("running dog.py")

### NEED TO MIX MATCH " AND ' CANT USE SAME ONE THRU OUT!
# print(f'does my dog snore? {sleep("beagle")}.')

##create my dog object
fido = Dog("fido")
fido.breed = 'lab'
print(fido.name)
fido.num_legs = 3
print(fido.num_legs)
#lbs_of_poop = fido.poop('raw_chicken')
#print(lbs_of_poop)
print(f"{fido.name} pooped {fido.poop('chocolate')} lbs")


# create a 2nd dog
corn = Dog('corn')
corn.breed = 'rodesian ridgeback'
timeb = corn.bark('mailman')
print(f"corn barked for {timeb} s")



print("End of line for dog.py")
