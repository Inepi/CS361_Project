from pyfiglet import Figlet
title = Figlet(font="slant")
print(title.renderText('FFXIV SPELL TOOL'))



def class_sel():
    ffxiv_classes = ["Paladin", "Warrior", "Dark Knight", "Gunbreaker", "White Mage", "Scholar", "Astrologian", "Sage", "Monk",
                     "Dragoon", "Ninja", "Samurai", "Reaper", "Bard", "Machinist", "Dancer", "Black Mage", "Summoner", "Red Mage"]
    ffxiv_roles = {"Tank":["Paladin", "Warrior", "Dark Knight", "Gunbreaker"], 
                   "Healer":["White Mage", "Scholar", "Astrologian", "Sage"],
                   "Melee DPS":["Monk","Dragoon", "Ninja", "Samurai", "Reaper"],
                   "Physical Ranged DPS":["Bard", "Machinist", "Dancer"], 
                   "Caster":["Black Mage", "Summoner", "Red Mage"],
                   }
    
    print("1. All Classes")
    print("2. Role Lookup")
    u_class_choice = input("Please select from the above choices to lookup a class, type the class name directly, or type 'exit' to exit: ")
    if u_class_choice == "1":
        for game_class in ffxiv_classes:
            print(game_class)
        u_class_choice = input("Which of the listed classes would you like to look up spells for?")
    elif u_class_choice == "2":
        print("The roles in the game are as follows: ")
        print("Tank, Healer, Melee DPS, Physical Ranged DPS, Caster")
        role_sel = input("Which of the following roles would you like to look up? ")
        print("Your selected role has the following classes: ")
        for game_c in ffxiv_roles[role_sel]:
            print(game_c)
        u_class_choice = input("Which of the listed classes would you like to look up spells for? ")
    elif u_class_choice == "exit":
        return
    
        

def main_menu():
    print("1. Class Selection")
    print("2. Spell Lookup")
    print("3. Experience Calculator")
    print("4. Exit Program")

def exp_calculator():
    exp_dict = {
    1:0,
    2:300,
    3:450,
    4:630,
    5:970,
    6:1440,
    7:1940,
    8:3000,
    9:3920,
    10:4970,
    11:5900,
    12:7430,
    13:8620,
    14:10200,
    15:11300,
    16:13100,
    17:15200,
    18:17400,
    19:19600,
    20:21900,
    21:24300,
    22:27400,
    23:30600,
    24:33900,
    25:37300,
    26:40800,
    27:49200,
    28:54600,
    29:61900,
    30:65600,
    31:68400,
    32:74000,
    33:82700,
    34:88700,
    35:95000,
    36:102000,
    37:113000,
    38:121000,
    39:133000,
    40:142000,
    41:155000,
    42:163000,
    43:171000,
    44:179000,
    45:187000,
    46:195000,
    47:214000,
    48:229000,
    49:244000,
    50:259000,
    51:421000,
    52:500000,
    53:580000,
    54:663000,
    55:749000,
    56:837000,
    57:927000,
    58:1019000,
    59:1114000,
    60:1211000,
    61:1387000,
    62:1456000,
    63:1534000,
    64:1621000,
    65:1720000,
    66:1834000,
    67:1968000,
    68:2126000,
    69:2137000,
    70:2550000,
    71:2923000,
    72:3018000,
    73:3153000,
    74:3324000,
    75:3532000,
    76:3770600,
    77:4066000,
    78:4377000,
    79:4777000,
    80:5256000,
    81:5992000,
    82:6171000,
    83:6942000,
    84:7205000,
    85:7948000,
    86:8287000,
    87:9231000,
    88:9529000,
    89:10459000,
    90:10838000,
    }

    
    user_level = int(input("Please enter your level: "))
    desired_level = int(input("Please enter your desired level: "))

    if desired_level < user_level:
        print("You can't go down in level!")
    elif desired_level == user_level:
        print("You're already at that level, so it would require 0 xp")
    elif desired_level > 90:
        print("The max level is currently 90, you can't go that high!")
    elif desired_level > user_level:
        lvl_dif = desired_level - user_level
        exp_tot = 0
        for i in range(1,lvl_dif+1):
            exp_tot += exp_dict[user_level+i]
        print(f"You would require {exp_tot} experience to hit level {desired_level}!")
    else:
        print("Sorry, I didn't understand your input.")

print(title.renderText('FFXIV SPELL TOOL'))
program_status = True
while program_status == True:
    main_menu()
    user_sel = int(input("Please make your selection: "))
    if user_sel == 1:
        class_sel()
    if user_sel == 2:
        print("This feature is currently being worked on!")
    if user_sel == 3:
        exp_calculator()
    if user_sel == 4:
        program_status = False
    print("\n")
print("Thank you for using the program!")
