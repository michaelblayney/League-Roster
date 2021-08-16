class League:
    def __init__(self, name):
        self.max_slots = 10
        self.slots = 0
        self.name = name
        self.followers = []

    def add_follower(self, name, ability, **kwargs):
        if(self.slots != self.max_slots):
            follower = Follower(name, ability, **kwargs)
            self.followers.append(follower)
            self.slots += 1

    def __str__(self):
        string = ""
        for i in self.followers:
            string = string + i.__str__() + "\n\n"
        return "**" + self.name + "**\n\n" + string + "[" + str(self.slots) + " slots used]"

    
class Stat:
    def __init__(self, rolls, dice_sides):
        self.rolls = rolls
        self.dice_sides = dice_sides

    def __str__(self):
        if(self.rolls == -1):
            return "---"
        if(self.rolls == 0):
            return "d" + str(self.dice_sides)
        return str(self.rolls) + "d" + str(self.dice_sides)

# :)
health = 0
brawl = 0
shoot = 0
dodge = 0
might = 0
finesse = 0
cunning = 0

class Follower:
    def __init__(self, name, ability, **kwargs):
        self.stats = {
            "health": Stat(0, 6),
            "brawl": Stat(1, 6),
            "shoot": Stat(1, 6),
            "dodge": Stat(1, 6),
            "might": Stat(1, 6),
            "finesse": Stat(1, 6),
            "cunning": Stat(1, 6)
        }
        self.name = name
        self.ability = ability
        self.distance = 12
        if(self.ability.ability_type == "AGILE"):
            self.stats["dodge"].rolls += 1
        elif(ability.ability_type == "ANIMAL"):
            self.stats["shoot"].rolls = -1
            for key, value in kwargs.items():
                self.stats[key.__str__()].rolls = value
        elif(self.ability.ability_type == "CLEVER"):
            self.stats["cunning"].rolls += 1
        elif(self.ability.ability_type == "FIERCE"):
            self.stats["brawl"].rolls += 1
        elif(self.ability.ability_type == "MARKSMAN"):
            self.stats["shoot"].rolls += 1
        elif(self.ability.ability_type == "MIGHTY"):
            self.stats["might"].rolls += 1
        elif(self.ability.ability_type == "SAVVY"):
            self.stats["finesse"].rolls += 1
        elif(ability.ability_type == "SPEEDY"):
            self.distance = 16

        #print(self)

    def __str__(self):
        string = self.name
        string += " (Follower) "
        string += "health=" + self.stats["health"].__str__() + " "
        string += "brawl=" + self.stats["brawl"].__str__() + " "
        string += "shoot=" + self.stats["shoot"].__str__() + " "
        string += "dodge=" + self.stats["dodge"].__str__() + " "
        string += "might=" + self.stats["might"].__str__() + " "
        string += "finesse=" + self.stats["finesse"].__str__() + " "
        string += "cunning=" + self.stats["cunning"].__str__() + " "
        string += "\n" + self.ability.__str__()
        return string


class Ability:
    def __init__(self, ability_type, description):
        self.ability_type = ability_type
        self.description = description

    def __str__(self):
        return self.description

AGILE = Ability("AGILE", "Agile - This character’s Dodge is increased by +1 die.")
ANIMAL = Ability("ANIMAL", "Animal - This character may not shoot, but adds +1d to two other skills.")
CLEVER = Ability("CLEVER", "Clever - This character’s Cunning is increased by +1 die.")
FIERCE = Ability("FIERCE", "Fierce - This character’s Brawl is increased by +1 die.")
MARKSMAN = Ability("MARKSMAN", "Marksman - This character’s Shoot is increased by +1 die.")
MIGHTY = Ability("MIGHTY", "Mighty - This character’s Might is increased by +1 die.")
SAVVY = Ability("SAVVY", "Savvy - This character’s Finesse is increased by +1 die.")
SPEEDY = Ability("SPEEDY", "Speedy - This character may run up to 16” — instead of 12”.")


if __name__ == '__main__':
    gog = League('Graveyard of Ghouls')
    gog.add_follower('Arg', AGILE)
    gog.add_follower('Brg', ANIMAL, brawl=2, might=2)
    gog.add_follower('Crg', CLEVER)
    gog.add_follower('Drg', FIERCE)
    gog.add_follower('Erg', MARKSMAN)
    gog.add_follower('Frg', MIGHTY)
    gog.add_follower('Grg', SAVVY)
    gog.add_follower('Hrg', SPEEDY)
    gog.add_follower('Irg', ANIMAL, brawl=2, dodge=2)
    gog.add_follower('Jrg', ANIMAL, might=2, dodge=2)

    print(gog)
