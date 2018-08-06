import random
import colorama
from .magic import Spell


# needed to add color to the terminal in VSCode
colorama.init()

# assigns variables to colors in terminal


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNiNG = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # needed to end the color code
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.items = items
        self.name = name
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n"+bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print("    "+str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n"+bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("    "+str(i) + ":", spell.name,
                  "(cost:", str(spell.cost)+")")
            i += 1

    def choose_items(self):
        i = 1
        print("\n"+bcolors.OKGREEN + bcolors.BOLD + "Items" + bcolors.ENDC)
        for item in self.items:
            print("    "+str(i) + ":", item["item"].name,
                  " - ", item["item"].description, " (x" + str(item["quantity"])+")")
            i += 1

    def get_stats(self):
        hp_bar = ""
        mp_bar = ""
        # health points bar calculation
        hp_bar_points = (self.hp/self.maxhp)*100/5
        while hp_bar_points > 0:
            hp_bar += "█"
            hp_bar_points -= 1
        while len(hp_bar) < 20:
            hp_bar += " "
        # magic points bar calculation
        mp_bar_points = (self.mp/self.maxmp)*100/10
        while mp_bar_points > 0:
            mp_bar += "█"
            mp_bar_points -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        # necessary to put empty spaces when the pontuation falls below a certain value
        hp_string = str(self.hp)+"/"+str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 9:
            decreased_hp = 9 - len(hp_string)
            while decreased_hp > 0:
                current_hp += " "
                decreased_hp -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp)+"/" + str(self.maxmp)
        current_mp = ""
        if len(mp_string) < 7:
            decreased_mp = 7 - len(mp_string)
            while decreased_mp > 0:
                current_mp += " "
                decreased_mp -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string

        print("NAME                      HP                        MP")
        print("                    ____________________               __________")
        print(bcolors.BOLD + self.name + ":     " + current_hp + " |" +
              bcolors.OKGREEN+hp_bar+bcolors.ENDC+bcolors.BOLD + "|     " +
              current_mp + " |"+bcolors.OKBLUE+mp_bar+bcolors.ENDC+"|")