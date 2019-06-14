import pymysql


try:
    conn = pymysql.connect("localhost", "root", "Ygdr@sil1418", "game")
    c = conn.cursor()
    print("ok")
except:
    print("only darkness")


def add():
    trap = marksmen = carrier = dodge = stealth = bloodbath = enchant = legacy = armor = castle = anesthetize = draw = 0
    name = input("name ")
    faction = input("faction ")
    rarity = int(input("rarity: 0 - token, 1 - common, 2 - uncommon, 3 - rare, 4 - unique, 5 - starter "))
    if rarity == 0:
        rarity = "token"
    elif rarity == 1:
        rarity = "common"
    elif rarity == 2:
        rarity = "uncommon"
    elif rarity == 3:
        rarity = "rare"
    elif rarity == 4:
        rarity = "unique"
    elif rarity == 5:
        rarity = "starter"
    display = input("display ")
    attack = int(input("attack "))
    health = int(input("health "))
    cost = int(input("cost "))
    sleep = int(input("sleep "))
    while(True):
        extra = input("extra abilites:AR - armor, AN - anesthetize, B - bloodbath, C - carrier, CA - castle, D - dodge, DR - draw, E - enchant,L - legacy, M - marksmen, S - Stealth, T - Trap, A - accept\n").upper()
        if extra == "T":
            trap = int(input("level "))
        elif extra == "M":
            marksmen = int(input("level "))
        elif extra == "C":
            carrier = int(input("level "))
        elif extra == "D":
            print("dodge added")
            dodge = 1
        elif extra == "S":
            print("stealth added")
            stealth = 1
        elif extra == "B":
            print("bloodbath added")
            bloodbath = 1
        elif extra == "E":
            enchant = int(input("level "))
        elif extra == "L":
            print("legacy added")
            legacy = 1
        elif extra == "AR":
            armor = int(input("level "))
        elif extra == "CA":
            print("castle added")
            castle = 1
        elif extra == "AN":
            print("anesthetize added")
            anesthetize = 1
        elif extra == "DR":
            draw = int(input("level"))
        elif extra == "A":
            break
    print("name: %s faction: %s rarity: %s display: %s\n attack %i health %i cost %i sleep %i\n extra: trap %i, marksmen %i, carrier %i, dodge %i, stealth %i, bloodbath %i, enchant %i, legacy %i, armor %i, castle %i, anesthetize %i, draw %i" % (name,faction,rarity,display,attack,health,cost,sleep,trap,marksmen,carrier,dodge,stealth,bloodbath,enchant,legacy,armor,castle, anesthetize,draw))
    while(True):
        wyb2 = input("Correct Y/N").upper()
        if wyb2 == "Y":
            c.execute("INSERT INTO cards(name,faction,rarity,display,attack,health,cost,sleep,trap,marksmen,carrier,dodge,stealth,bloodbath,enchant,legacy,armor,castle,anesthetize,draw) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (name,faction,rarity,display,attack,health,cost,sleep,trap,marksmen,carrier,dodge,stealth,bloodbath,enchant,legacy,armor,castle,anesthetize,draw))
            conn.commit()
            print("completed")
            break
        elif wyb2 == "N":
            print("as you wish")
            break

while(True):
    wyb = input("A - add, Q - quit").upper()
    if wyb == "A":
        add()
    elif wyb == "Q":
        break