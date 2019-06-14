import pymysql
import random

p_deck = []
p_deck_add = []
p_hand = []
p_discard = []
o_cards = []
ready = 1
d = 4

class Opp:
    def __init__(self,name,health):
        self.name = name
        self.health = health
    def start(self):
        if self.name == "kobold":
            c.execute("SELECT * FROM cards WHERE display = 'bt' OR display = 'kw'")
            wish2 = c.fetchall()
            for row in wish2:
                o_cards.append(row)
        if self.name == "trickster":
            c.execute("SELECT * FROM cards WHERE display = 'na' OR display = 'pi' OR display = 'pa'")
            wish2 = c.fetchall()
            for row in wish2:
                o_cards.append(row)
        if self.name == "squire":
            c.execute("SELECT * FROM cards WHERE display = 'ca' OR display = 'sq'")
            wish2 = c.fetchall()
            for row in wish2:
                o_cards.append(row)
            print(o_cards)
    def move(self,cool):
        t = m = 0
        if self.name == "kobold":
            for i in p_info:
                if i != []:
                    t += 1
            if t > 3 and cool[0] == 0:
                p = 0
                for e in range(0,8):
                    play(p,o_cards[0])
                    p += 1
                cool[0] = 3
            else:
                for i in o_info:
                    if i != []:
                        m += 1
                for w in range(3):
                    if m == 8:
                        break
                    while(True):
                        u = random.randrange(0,8)
                        if o_side[u] == ["#", '##', "#"]:
                            card = random.choice(o_cards)
                            play(u,card)
                            m += 1
                            break
        if self.name == "trickster":
            t = n = 0
            for i in o_info:
                if i != []:
                    n += 1
            if n != 8:
                for i in p_stats:
                    if p_side[t] != ["#", '##', "#"]:
                        if i[5] > 2:
                            m = 1
                            break
                    t += 1
                if m == 1 and cool[0] == 0:
                    cool[0] = 3
                    x = play(t,o_cards[1])
                    if x == 0:
                        t2 = 0
                        for e in o_side:
                            if e ==["#,##,#"]:
                                play(t2,o_cards[1])
                            t2 += 1
                    elif x == 1:
                        if t-1 >= 0:
                            t -= 1
                            play(t,o_cards[2])
                            t += 1
                        if t+1 < 8:
                            t += 1
                            play(t,o_cards[2])
                            t -= 1
                elif cool[2] == 0:
                    cool[2] = 2
                    t2 = 0
                    for e in o_side:
                        if e == ["#","##","#"]:
                            play(t2,o_cards[1])
                            break
                        t2 += 1
                    t3 = 7
                    for r in range(7):
                        if t3 < 0:
                            break
                        if o_side[t3] == ["#","##","#"]:
                            play(t3,o_cards[1])
                            break
                        t3 -= 1
                else:
                    for w in range(3):
                        if n == 8:
                            break
                        while(True):
                            u = random.randrange(0,8)
                            if o_side[u] == ["#", '##', "#"]:
                                play(u,o_cards[0])
                                n += 1
                                break
        if self.name == "squire":
            if cool[0] == 0:
                cool[0] = 2
                for i in o_info:
                    if i != []:
                        m += 1
                if m != 8:
                    t = 0
                    for e in o_side:
                        if e == ["#","##","#"]:
                            play(t,o_cards[1])
                            break
                        t += 1
                    for w in range(2):
                        if m == 8:
                            break
                        while(True):
                            u = random.randrange(0,8)
                            if o_side[u] == ["#", '##', "#"]:
                                play(u,o_cards[0])
                                m += 1
                                break
            else:
                for i in o_info:
                    if i != []:
                        m += 1
                for w in range(3):
                    if m == 8:
                        break
                    while(True):
                        u = random.randrange(0,8)
                        if o_side[u] == ["#", '##', "#"]:
                            play(u,o_cards[0])
                            m += 1
                            break



dummy = Opp("dummy",5)
kobold = Opp("kobold", 10)
trickster = Opp("trickster", 10)
squire = Opp("squire", 10)

print("sql connect")
login = input("login\n")
password = input("password\n")

try:
    conn = pymysql.connect("localhost", login, password, "game")
    c = conn.cursor()
    print("Get ready")
except:
    print("only darkness")
    ready = 0

def death(side,position):
    tr = dlevel = 0
    if side == "p":
        if p_stats[position][16] > 0:
            legacy("p",position)
        else:    
            p_side[position] = ["#", "##", "#"]
            p_side2[position] = ["#", "#", "#", "#"]
            if p_info[position][9] != 0:
                tr = 1
                dlevel = p_info[position][9]
            if p_info[position][3] != "token":
                p_discard.append(p_info[position])
            p_info[position] = []
            p_stats[position].clear()
            if tr == 1:
                trap("o",position,dlevel)
    if side == "o":
        if o_stats[position][16] > 0:
            legacy("o",position)
        else:
            if o_info[position][9] != 0:
                tr = 1
                dlevel = o_info[position][9]
            o_side[position] = ["#", "##", "#"]
            o_side2[position] = ["#", "#", "#", "#"]
            o_info[position] = []
            o_stats[position].clear()
            if tr == 1:
                trap("o",position,dlevel)
    
def play(wyb4,i):
    if o_side[wyb4] == ["#",'##',"#"]:
        o_side[wyb4][0] = i[5]
        o_side[wyb4][1] = i[4]
        o_side[wyb4][2] = i[6]
        o_info[wyb4] = i
        if i[9] != 0:
            t = 0
            for u in o_side2[wyb4]:
                if u == "#":
                    o_side2[wyb4][t] = "t"
                    o_side2[wyb4][t+1] = i[9]
                    break
                t += 1
        if i[12] != 0:
            t = 0
            for u in o_side2[wyb4]:
                if u == "#":
                    o_side2[wyb4][t] = "d"
                    o_side2[wyb4][t+1] = "*"
                    break
                t += 1
        if i[13] != 0:
            t = 0
            for u in o_side2[wyb4]:
                if u == "#":
                    o_side2[wyb4][t] = "s"
                    o_side2[wyb4][t+1] = "*"
                    break
                t += 1
        if i[14] != 0:
            t = 0
            for u in o_side2[wyb4]:
                if u == "#":
                    o_side2[wyb4][t] = "b"
                    o_side2[wyb4][t+1] = "*"
                    break
                t += 1
        if i[15] != 0:
            enchant("o",wyb4,i[15])
        if i[16] != 0:
            t = 0
            for u in o_side2[wyb4]:
                if u == "#":
                    o_side2[wyb4][t] = "l"
                    o_side2[wyb4][t+1] = "*"
                    break
                t += 1
        if i[17] != 0:
            t = 0
            for u in o_side2[wyb4]:
                if u == "#":
                    o_side2[wyb4][t] = "a"
                    o_side2[wyb4][t+1] = i[17]
                    break
                t += 1
        if i[18] != 0:
            t = 0
            for u in o_side2[wyb4]:
                if u == "#":
                    o_side2[wyb4][t] = "c"
                    o_side2[wyb4][t+1] = "*"
                    break
                t += 1
        if i[19] != 0:
            anesthetize("o")
        for j in o_info[wyb4]:
            o_stats[wyb4].append(j)
        battlefield()
        return(1)
    else:
        return(0)

def intro():
    print("-"*144)
    print("Many years ago, world was engulfed in global war. Factions danced to the chaotic music of steel, magic and blood,\nalliances were created and broken, until ... king has crowned himself.\nInsane wizard Yex conducted ritual that gave him the power of god and his first decree forbid fighting, those who didn't listen died in horrible ways.\nPeace lasted for hundred years, but now he disappeared, his house open and who knows maybe description of ritual is still there?")
    print("-"*144)
    print("Factions:")
    print("Machine:\nThe ever growing army, created by dying race to continue their work and conquer everything.\nIn fight they want overhelm opponent by sheer numbers, supplemented by cover fire and booby traps in areas they lost control.\nUnique keywords:\n-Marksmen: deals x damage to opposite creature or opponent if there is nothing there.\n-Trap: after dying deals x damage to every creature near them.\n-Carrier: if possible creates token of x attack and health to the left and right.\n")
    print("Fey:\nBorn from pure magic, inteligent but without morality. Fallen from position of gods playing with mortals, will do anything to get it back.\nIn fight they use mostly weak but hard to deal with units, and shamans with ability to enchant others.\nUnique keywords:\n-Anesthetize: opposite creature falls asleep and can't attack next turn.\n-Enchant: creatures to the left and right dain +x attack and health.\n-Dodge: when attacked creature wil try to move left.\n")
    print("Aliance(not ready):\nSaved by Yex from extinction humans, dwarfs and nagas didn't want to make the same mistake they ancestor did and was preparing to next war, making this weard aliance to increase chances. Now they are ready to hunt their previous hunters.\nIn fight their units are not the strongest, but with their equipment they can reduce damage and attack more than one enemy creature, while using nagas abilities to suprise attack their opponents.\nUnique Keyword:\n-Armor: reduce damage from attack by x.\n-Unit: can also attack opponents creatures to the right and left.\n-Bloodbath: creature first attack deals double damage.\n")
    print("Giants(not ready):\nAncient but lazy, nobody really cared about them, but recently new warchief appeard and he will do what he has to, to make a real threat out of them.\nIn fight giants use powerful but costly creatures quite often with ability to deal damage to enemy even if blocked, most of their cheaper unit have some downsides.\nUnique keywords:\n-Lazy: needs x more turns to get ready and attack.\n-Rage: gain +x attack and health, after surviving damage.\n-Giant: if they deal more damage than opposite creture has, rest is transfered to opponent.\n")

def battlefield():
    for e in o_side2:
        for i in e:
            print(i, end="")
        print("", end=" ")
    print("")
    t = 0
    for e in o_side:
        if e != ["#","##","#"]:
            e[2] = o_stats[t][6]
            e[0] = o_stats[t][5]
        t += 1
        for i in e:
            print(i, end="")
        print("", end=" ")
    print(" %s health: %i \n " % (opp.name, opp.health))
    t = 0
    for e in p_side:
        if e != ["#", "##", "#"]:
            e[2] = p_stats[t][6]
            e[0] = p_stats[t][5]
        t += 1
        for i in e:
            print(i, end="")
        print("", end=" ")
    print(" %s health: %i" % (name, p_health))
    for e in p_side2:
        for i in e:
            print(i, end="")
        print("", end=" ")
    print("\n")

def sorte(val):
    return(val[1])

def fend():
    t = 0
    for i in p_side:
        if i != ["#","##","#"]:
            death("p",t)
        t += 1
    for e in p_discard:
        p_deck.append(e)
    p_discard.clear()
    for w in p_hand:
        p_deck.append(w)
    p_hand.clear()
    p_deck.sort(key = sorte)

def attack(side,health):
    if side == "p":
        a = t = 0
        for i in p_side:
            b = 1
            if i != ["#","##","#"]:
                if p_stats[t][8] > 0:
                    p_stats[t][8] -= 1
                else:
                    if p_stats[t][13] != 0:
                        p_stats[t][13] = 0
                        t2 = 0
                        for u in p_side2[t]:
                            if u == "s":
                                p_side2[t][t2] = "#"
                                p_side2[t][t2+1] = "#"
                                break
                            t2 += 1
                    if p_stats[t][14] != 0:
                        p_stats[t][14] = 0
                        b = 2
                        t2 = 0
                        for u in p_side2[t]:
                            if u == "b":
                                p_side2[t][t2] = "#"
                                p_side2[t][t2+1] = "#"
                                break
                            t2 += 1
                    tc = tc2 = 0
                    for i in o_stats:
                        if i != []:
                            if i[18] > 0:
                                tc2 = 1
                                break
                        tc += 1
                    if tc2 > 0:
                        if o_stats[tc][17] > 0:
                                a = o_stats[tc][17]
                        if b*p_stats[t][5]-a > 0:
                            o_stats[tc][6] -= b*p_stats[t][5]-a
                        if o_stats[tc][6] <= 0:
                            death("o",tc)
                    elif o_side[t] == ["#","##","#"] or o_stats[t][13] > 0:
                        opp.health -= b*p_stats[t][5]
                        if opp.health <= 0:
                            break
                    elif o_stats[t][12] > 0:
                        x = dodge("o",t)
                        if x == 1:
                            opp.health -= b*p_stats[t][5]
                            if opp.health <= 0:
                                break
                        if x == 0:
                            if o_stats[t][17] > 0:
                                a = o_stats[t][17]
                            if b*p_stats[t][5]-a > 0:
                                o_stats[t][6] -= b*p_stats[t][5]-a
                            if o_stats[t][6] <= 0:
                                death("o",t)
                    else:
                        if o_stats[t][17] > 0:
                                a = o_stats[t][17]
                        if b*p_stats[t][5]-a > 0:
                            o_stats[t][6] -= b*p_stats[t][5]-a
                        if o_stats[t][6] <= 0:
                            death("o",t)

            t += 1
    elif side == "o":
        a = t = 0
        for i in o_side:
            b=1
            if i != ["#", "##", "#"]:
                if o_stats[t][8] > 0:
                    o_stats[t][8] -= 1
                else:
                    if o_stats[t][13] != 0:
                        o_stats[t][13] = 0
                        t2 = 0
                        for u in p_side2[t]:
                            if u == "s":
                                o_side2[t][t2] = "#"
                                o_side2[t][t2+1] = "#"
                                break
                            t2 += 1
                    if o_stats[t][14] != 0:
                        o_stats[t][14] = 0
                        b=2
                        t2 = 0
                        for u in p_side2[t]:
                            if u == "b":
                                o_side2[t][t2] = "#"
                                o_side2[t][t2+1] = "#"
                                break
                            t2 += 1
                    tc = tc2 = 0
                    for i in p_stats:
                        if i != []:
                            if i[18] > 0:
                                tc2 = 1
                                break
                        tc += 1
                    if tc2 > 0:
                        if p_stats[tc][17] > 0:
                                a = p_stats[tc][17]
                        if b*o_stats[t][5]-a > 0:
                            p_stats[tc][6] -= b*o_stats[t][5]-a
                        if p_stats[tc][6] <= 0:
                            death("p",tc)
                    elif p_side[t] == ["#", "##", "#"] or p_stats[t][13] > 0:
                        health -= b*o_stats[t][5]
                        if p_health <= 0:
                            break
                    elif p_stats[t][12] > 0:
                        x = dodge("p",t)
                        if x == 1:
                            health -= b*o_stats[t][5]
                            if p_health <= 0:
                                break
                        if x == 0:
                            if p_stats[t][17] > 0:
                                a = p_stats[t][17]
                            if b*o_stats[t][5]-a > 0:
                                p_stats[t][6] -= b*o_stats[t][5] - a
                            if p_stats[t][6] <= 0:
                                death("p",t)
                    else:
                        if p_stats[t][17] > 0:
                                a = p_stats[t][17]
                        if b*o_stats[t][5]-a > 0:
                            p_stats[t][6] -= b*o_stats[t][5] - a
                        if p_stats[t][6] <= 0:
                            death("p",t)

            t += 1
        return(health)

def marksmen(side):
    if side == "p":
        if o_side[wyb4] == ["#", "##", "#"] or o_stats[wyb4][13] > 0:
            opp.health -= p_info[wyb4][10]
        else:
            o_stats[wyb4][6] -= p_info[wyb4][10]
            if o_stats[wyb4][6] <= 0:
                death("o",wyb4)

def trap(side,position,dlevel):
    if side == "p":
        if position-1 >= 0:
            if p_side[position-1] != ["#", "##", "#"]:
                p_stats[position-1][6] -= dlevel
                if p_stats[position-1][6]  <= 0:
                    death("p",position-1)
            if o_side[position - 1] != ["#", "##", "#"]:
                o_stats[position - 1][6] -= dlevel
                if o_stats[position - 1][6] <= 0:
                    death("o", position - 1)
        if position +1 <= 7:
            if p_side[position + 1] != ["#", "##", "#"]:
                p_stats[position + 1][6] -= dlevel
                if p_stats[position + 1][6] <= 0:
                    death("p", position + 1)
            if o_side[position + 1] != ["#", "##", "#"]:
                o_stats[position + 1][6] -= dlevel
                if o_stats[position + 1][6] <= 0:
                    death("o", position + 1)
        if o_side[position] != ["#", "##", "#"]:
            o_stats[position][6] -= dlevel
            if o_stats[position][6] <= 0:
                death("o", position)
    if side == "o":
        if position-1 >= 0:
            if p_side[position-1] != ["#", "##", "#"]:
                p_stats[position-1][6] -= dlevel
                if p_stats[position-1][6]  <= 0:
                    death("p",position-1)
            if o_side[position - 1] != ["#", "##", "#"]:
                o_stats[position - 1][6] -= dlevel
                if o_stats[position - 1][6] <= 0:
                    death("o", position - 1)
        if position +1 <= 7:
            if p_side[position + 1] != ["#", "##", "#"]:
                p_stats[position + 1][6] -= dlevel
                if p_stats[position + 1][6] <= 0:
                    death("p", position + 1)
            if o_side[position + 1] != ["#", "##", "#"]:
                o_stats[position + 1][6] -= dlevel
                if o_stats[position + 1][6] <= 0:
                    death("o", position + 1)
        if p_side[position] != ["#", "##", "#"]:
            p_stats[position][6] -= dlevel
            if p_stats[position][6] <= 0:
                death("p", position)

def carrier(side):
    drop = [0,"Mecha-Scarab","Machine","token","ms",i[11],i[11],0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if side == "p":
        if wyb4-1 >= 0: 
            if p_side[wyb4-1] == ["#","##","#"]:
                p_side[wyb4-1][0] = drop[5]
                p_side[wyb4-1][1] = drop[4]
                p_side[wyb4-1][2] = drop[6]
                p_side[wyb4-1] = drop
            for j in p_info[wyb4-1]:
                p_stats[wyb4-1].append(j)
        if wyb4+1 <= 7: 
            if p_side[wyb4+1] == ["#","##","#"]:
                p_side[wyb4+1][0] = drop[5]
                p_side[wyb4+1][1] = drop[4]
                p_side[wyb4+1][2] = drop[6]
                p_info[wyb4+1] = drop
            for j in p_info[wyb4+1]:
                p_stats[wyb4+1].append(j)

def dodge(side,position):
    if side == "p":
        if (position-1) >= 0:
            if p_side[position-1] == ["#","##","#"]:
                p_side[position-1] = [p_stats[position][5],p_stats[position][4],p_stats[position][6]]
                t = 0
                for w in p_side2[position]:
                    if w == "#":
                        break
                    else:
                        p_side2[position-1][t] = w
                for i in p_info[position]:
                    p_info[position-1].append(i)
                for e in p_stats[position]:
                    p_stats[position-1].append(e)
                p_side[position] = ["#", "##", "#"]
                p_side2[position] = ["#", "#", "#", "#"]
                p_info[position] = []
                p_stats[position].clear()
                return(1)
            else:
                return(0)
    if side == "o":
        if (position+1) <= 7:
            if o_side[position+1] == ["#","##","#"]:
                o_side[position+1] = [o_stats[position][5],o_stats[position][4],o_stats[position][6]]
                t = 0
                for w in o_side2[position]:
                    if w == "#":
                        break
                    else:
                        o_side2[position+1][t] = w
                for i in o_info[position]:
                    o_info[position+1].append(i)
                for e in o_stats[position]:
                    o_stats[position+1].append(e)
                o_side[position] = ["#", "##", "#"]
                o_side2[position] = ["#", "#", "#", "#"]
                o_info[position] = []
                o_stats[position].clear()
                return(1)
            else:
                return(0)

def enchant(side,pos,elevel):
    if side =="p":
        if pos-1 >= 0:
            if p_side[pos-1] != ["#","##","#"]:
                p_stats[pos-1][5] += elevel
                p_stats[pos-1][6] += elevel
        if pos+1 < 8:
            if p_side[pos+1] != ["#","##","#"]:
                p_stats[pos+1][5] += elevel
                p_stats[pos+1][6] += elevel
    if side =="o":
        if pos-1 >= 0:
            if o_side[pos-1] != ["#","##","#"]:
                o_stats[pos-1][5] += elevel
                o_stats[pos-1][6] += elevel
        if pos+1 < 8:
            if o_side[pos+1] != ["#","##","#"]:
                o_stats[pos+1][5] += elevel
                o_stats[pos+1][6] += elevel

def legacy(side,position):
    tr = 0
    if side == "p":
        p_stats[position].clear()
        for i in p_info[position]:
            p_stats[position].append(i)
        if p_info[position][9] != 0:
            tr = 1
            dlevel = p_info[position][9]
        if p_info[position][3] != "token":
            p_discard.append(p_info[position])
        if tr == 1:
            trap("o",position,dlevel)
        p_stats[position][3] = "token"
        p_stats[position][8] = 0
        p_stats[position][16] = 0
        t = 0
        for i in p_side2[position]:
            if i == "l":
                p_side2[position][t] = "#"
                p_side2[position][t+1] = "#"
                break
            t += 1
    if side == "o":
        o_stats[position].clear()
        for i in o_info[position]:
            o_stats[position].append(i)
        if o_info[position][9] != 0:
            tr = 1
            dlevel = o_info[position][9]
        if tr == 1:
            trap("o",position,dlevel)
        o_stats[position][3] = "token"
        o_stats[position][16] = 0
        for i in o_side2[position]:
            if i == "l":
                o_side2[position][t] = "#"
                o_side2[position][t+1] = "#"
                break
            t += 1
            
def anesthetize(side):
    if side == "p":
        if o_side[wyb4] != ["#","##","#"]:
            o_stats[wyb4][8] += 1
    if side == "o":
        if p_side[wyb4] != ["#","##","#"]:
            p_stats[wyb4][8] += 1

def look(purpose):
    for i in purpose:
        if i != []:
            print("name: %s | faction: %s | rarity: %s | display: %s | attack: %i | health: %i | cost: %i | abilities:" % (i[1],i[2],i[3],i[4],i[5],i[6],i[7]), end=" ")
            if i[8] == 0:
                print("prepared", end=" ")
            elif i[8] > 1:
                print("lazy: %i" % i[8], end=" ")
            if i[9] != 0:
                print("trap: %i" % i[9], end=" ")
            if i[10] != 0:
                print("marksmen: %i" % i[10], end=" ")
            if i[11] != 0:
                print("carrier: %i" % i[11], end=" ")
            if i[12] != 0:
                print("dodge", end=" ")
            if i[13] != 0:
                print("stealth", end=" ")
            if i[14] != 0:
                print("bloodbath", end=" ")
            if i[15] != 0:
                print("enchant: %i" % i[15], end=" ")
            if i[16] != 0:
                print("legacy", end=" ")
            if i[17] != 0:
                print("armor: %i" % i[17], end=" ")
            if i[18] != 0:
                print("castle", end=" " )
            if i[19] != 0:
                print("anesthetize", end=" ")
            if i[20] != 0:
                print("draw: %i" % i[20], end=" ")
            print( )

def draw(a):
    for i in range(a):
        if len(p_deck) == 0:
            if len(p_discard) == 0:
                break
            else:
                for o in p_discard:
                    p_deck.append(o)
                p_discard.clear()
        chosen = random.choice(p_deck)
        p_hand.append(chosen)
        p_deck.remove(chosen)

def kdictonary():
    print("-"*144)
    print("note: x/x means attack and health.")
    print("Anesthetize - opposite creature can't attack next turn")
    print("Armor - minion receives x less damage from attacks (a*)")
    print("Bloodbath - minion deals double damage during first attack. (b*)")
    print("Castle - as long as minion with this exist, every enemy attack deals damage to it (c*)")
    print("Carrier x - if possible minion summons mecha-scarabs x/x to the left and right of its position.")
    print("Dodge - if possible before being attacked move to the left. (d*)")
    print("Draw - when played, you draw x card")
    print("Enchant x - if possible gives +x/+x to minions on the right and left of its position.")
    print("Legacy - minion summons its copy without this keyword after dying. (*l)")
    print("Marksmen x - deal x damage to opposite minion or if there isn't one to the opponent.")
    print("Prepared - minion is able to atack, as keyword it means that minioon can attack without waiting turn")
    print("Stealth - minion can't be targeted by attacks or abilities during it's first turn (for most cases it just isn't there). (*s)")
    print("Trap x - minion deals x damage to every creature in nearby slot after dying (yes, that means diagonally and to the left and right.")
    print("-"*144)

def spoils():
    choices = []
    for i in range(3):
        while(True):
            reward = []
            x = random.randint(0,100)
            y = random.randint(0,10)
            if x <= 70 and y < 7:
                c.execute("SELECT * FROM cards WHERE rarity = 'common' and faction = %s", faction)
            elif x > 70 and x <= 90 and y < 7:
                c.execute("SELECT * FROM cards WHERE rarity = 'uncommon' and faction = %s", faction)
            elif x > 90 and y < 7:
                c.execute("SELECT * FROM cards WHERE rarity = 'rare' and faction = %s", faction)
            elif x <= 70 and y >= 7:
                c.execute("SELECT * FROM cards WHERE rarity = 'common' and faction = 'Neutral'")
            elif x > 70 and x <= 90 and y >= 7:
                c.execute("SELECT * FROM cards WHERE rarity = 'uncommon' and faction = 'Neutral'")
            elif x > 90 and y >= 7:
                c.execute("SELECT * FROM cards WHERE rarity = 'rare' and faction = 'Neutral'")
            wish2 = c.fetchall()
            for row in wish2:
                reward.append(row)
            choice = random.choice(reward)
            if i == 0:
                break
            if i == 1:
                if choice != choices[0]:
                    break
            if i == 2:
                if choice != choices[0] and choice != choices[1]:
                    break
        choices.append(choice)
    print(choices)
    look(choices)
    while(True):
        wybk = input("which card you want to add, 1,2,3 or q if you don't want any \n")
        if wybk == "1":
            p_deck.append(choices[0])
            p_deck_add.append(choices[0])
            break
        elif wybk == "2":
            p_deck.append(choices[1])
            p_deck_add.append(choices[1])
            break
        elif wybk == "3":
            p_deck.append(choices[2])
            p_deck_add.append(choices[2])
            break
        elif wybk == "q":
            break

e = ng = 0
while(ready == 1):
    p = 0
    if e == 1:
        break
    if ng == 0:
        print("Menu")
        wyb = input("N - New game\nL - Load Game\nT - Tutorial\nQ - Quit \n").upper()
    if wyb == "N":
        if ng == 0:
            print("b to go back")
            level = 0
            name = input("name \n")
        if name == "b":
            continue
        c.execute("SELECT * FROM players")
        find = c.fetchall()
        for row in find:
            if name == row[1]:
                delet = row[0]
                p = 1
                break
        if p == 0:
            intro()
            while(True):
                faction = input("faction:\n")
                if faction == "b":
                    break
                print("Name: %s Faction: %s" % (name,faction))
                wyb2 = input("Correct Y/N\n" ).upper()
                if wyb2 == "Y":
                    if faction == "Machine":
                        c.execute("INSERT INTO players(name,faction,level) VALUES (%s,%s,%s)", (name,faction,level))
                        c.execute("SELECT * FROM players")
                        find = c.fetchall()
                        for row in find:
                            if name == row[1]:
                                id = row[0]
                                break
                        c.execute("INSERT INTO deck(player_id,card_id,quantity) VALUES (%s,%s,%s)", (id,1,4))
                        c.execute("INSERT INTO deck(player_id,card_id,quantity) VALUES (%s,%s,%s)", (id,2,4))
                        c.execute("INSERT INTO deck(player_id,card_id,quantity) VALUES (%s,%s,%s)", (id,3,1))
                        c.execute("INSERT INTO deck(player_id,card_id,quantity) VALUES (%s,%s,%s)", (id,4,1))
                        conn.commit()
                        d = e = 1
                        c.execute("SELECT * FROM players")
                        find = c.fetchall()
                        for row in find:
                            if name == row[1]:
                                id = row[0]
                                name = row[1]
                                faction = row[2]
                                level = int(row[3])
                                d = e = 1
                                c.execute("SELECT * FROM deck WHERE player_id = %s", id)
                                wish = c.fetchall()
                                c.execute("SELECT * FROM cards")
                                wish2 = c.fetchall()
                                for row2 in wish:
                                    for row3 in wish2:
                                        if row2[1] == row3[0]:
                                            for i in range(row2[2]):
                                                p_deck.append(row3)
                        print("completed")
                        break
                    if faction == "Fey":
                        c.execute("INSERT INTO players(name,faction,level) VALUES (%s,%s,%s)", (name,faction,level))
                        c.execute("SELECT * FROM players")
                        find = c.fetchall()
                        for row in find:
                            if name == row[1]:
                                id = row[0]
                                break
                        c.execute("INSERT INTO deck(player_id,card_id,quantity) VALUES (%s,%s,%s)", (id,7,4))
                        c.execute("INSERT INTO deck(player_id,card_id,quantity) VALUES (%s,%s,%s)", (id,9,4))
                        c.execute("INSERT INTO deck(player_id,card_id,quantity) VALUES (%s,%s,%s)", (id,10,1))
                        c.execute("INSERT INTO deck(player_id,card_id,quantity) VALUES (%s,%s,%s)", (id,11,1))
                        conn.commit()
                        d = e = 1
                        c.execute("SELECT * FROM players")
                        find = c.fetchall()
                        for row in find:
                            if name == row[1]:
                                id = row[0]
                                name = row[1]
                                faction = row[2]
                                level = int(row[3])
                                d = e = 1
                                c.execute("SELECT * FROM deck WHERE player_id = %s", id)
                                wish = c.fetchall()
                                c.execute("SELECT * FROM cards")
                                wish2 = c.fetchall()
                                for row2 in wish:
                                    for row3 in wish2:
                                        if row2[1] == row3[0]:
                                            for i in range(row2[2]):
                                                p_deck.append(row3)
                        print("completed")
                        break
                elif wyb2 == "N":
                    print("as you wish")
        else:
            print("name already exist")
            x = input("Are you sure you want to override? Y/N\n").upper()
            if x == "Y":
                print("as you wish")
                c.execute("DELETE FROM players WHERE idplayers=%s", delet)
                conn.commit()
                ng = 1
    if wyb == "L":
        wyb2 = input("name \n")
        c.execute("SELECT * FROM players")
        find = c.fetchall()
        for row in find:
            if wyb2 == row[1]:
                id = row[0]
                name = row[1]
                faction = row[2]
                level = int(row[3])
                d = e = 1
                c.execute("SELECT * FROM deck WHERE player_id = %s", id)
                wish = c.fetchall()
                c.execute("SELECT * FROM cards")
                wish2 = c.fetchall()
                for row2 in wish:
                    for row3 in wish2:
                        if row2[1] == row3[0]:
                            for i in range(row2[2]):
                                p_deck.append(row3)
                break
        if e == 0:
            print("name not found")
    elif wyb == "T":
        opp = dummy
        o_info = [[], [], [], [], [], [], [], []]
        o_stats = [[], [], [], [], [], [], [], []]
        o_side2 = [["#","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","#"]]
        o_side = [["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"]]
        p_side = [["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"]]
        p_side2 = [["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"],["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"]]
        p_info = [[], [], [], [], [], [], [], []]
        p_stats = [[], [], [], [], [], [], [], []]
        p_health = 15
        name = "Player"
        battlefield()
        print("Hello, welcome to tutorial.")
        print("Thing up there is called battlefied, it's right side displays health, to win fight you need to reduce your opponent health to zero or less, while maintaining yours above that level.")
        input("enter to continue")
        print("Left side has minion slots, one looks like that:")
        print("####\n####")
        print("and after minion was played, it looks like that:")
        print("3dw4\na1##")
        input("continue")
        print("first number (3) represents attack or in other words how much damage minion will deal to opposing creature, if there is no opposing creature it will deal damage to opponent.")
        input("continue")
        print("two letters (dw) are unique identificator of unit, that's with little practise should let you recognise what it is without trouble.")
        input("continue")
        print("second number (4) represents health or how much damage minion can take before dying.")
        input("continue")
        print("second row shows abilities, in this case unit has armor (a), so it reduces attack damage dealt to it by one (1).\nSome abilities doens't have levels they will be shown like that (l*).\nImportant to note is that it won't show abilities that only activate after playing card like marksmen(deal x damage),\nabilities that was spent like bloodbath( deal twice as much damage in first attack) also won't be displayed")
        input("continue")
        print("now that you know what this signs means you are probably wondering how to actually play? I will explain in a few simple steps:")
        print("-Draw: at the start of turn you draw four from your deck, if there is not enough card discard pile will be shuffled into deck.")
        input("continue")
        print("-Play: choose minion (by writing they identificator) and position, after playing everything you want write end.\nImportant: every minion has a cost and you can't spend more than you have power.")
        input("continue")
        print("-Attack: minions deal their damage to opposite character or opponent\nImportant: most minions can't attack immadietly after being played.")
        input("continue")
        print("-Discard: you discard everything you didn't play.")
        input("continue")
        print("-Opponent move\n-Repeat\nSimple isn't it?")
        input("continue")
        input("If you win fight as reward you can choose card or cards to add to your deck and gain exp,\nwhen you gather enough you will level up meaning that your health pool beacame larger and opponents will become more dangerous.\ncontinue")
        input('Now you might think "that doesnt\'t sound like good deal" and you will be right, but to win this game you have to get to the seventh level and win with last boss, so good luck.')
    elif wyb == "Q":
        d = 4
        break

while(d != 4 and ready == 1):
    """
    c.execute("SELECT * FROM cards WHERE idcards = 1 OR idcards = 5")
    wish2 = c.fetchall()
    for row in wish2:
        p_deck_add.append(row)
    print(p_deck_add)
    """

    print("%s %s level: %i" % (name,faction,level))
    print("What do you want to do?")
    wyb = input("F - fight, S - Save, D - Deck, K - Keyword Dictonary, Q - Quit\n").upper()
    if wyb == "F":
        while(True):
            wyb2 = input("choose opponent: kobold,squire or trickster\n")
            if wyb2 == "kobold":
                opp = kobold
                break
            elif wyb2 == "squire":
                opp = squire
                break
            elif wyb2 == "trickster":
                opp = trickster
                break
        ap = [0,0,1,2,3]
        o_info = [[], [], [], [], [], [], [], []]
        o_stats = [[], [], [], [], [], [], [], []]
        o_side2 = [["#","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","#"],["#","#","#","#"]]
        o_side = [["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"]]
        p_side = [["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"],["#","##","#"]]
        p_side2 = [["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"],["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"], ["#", "#", "#", "#"]]
        p_info = [[], [], [], [], [], [], [], []]
        p_stats = [[], [], [], [], [], [], [], []]
        p_health = 15 + 5*level
        opp.start()
        while(True):
            
            print("-"*144)
            draw(4)
            power = 3
            while(True):
                battlefield()
                look(p_hand)
                wyb3 = input("choose card to play (write display), power left: %i, end to end turn, l to look \n" % power).lower()
                if wyb3 == "end":
                    break
                elif wyb3 == "l":
                    while(True):
                        wyb4 = input("what do you want to see? h - hand, de - decksize, di - discard, os - opponent minions, ps - player minions, k - keyword dictonary, end \n").lower()
                        if wyb4 == "h":
                            look(p_hand)
                        elif wyb4 == "de":
                            print(len(p_deck))
                        elif wyb4 == "di":
                            look(p_discard)
                        elif wyb4 == "os":
                            look(o_stats)
                        elif wyb4 == "ps":
                            look(p_stats)
                        elif wyb4 == "k":
                            kdictonary()
                        elif wyb4 == "end":
                            break
                else:
                    for i in p_hand:
                        if wyb3 == i[4]:
                            if power < i[7]:
                                print("not enough power")
                            else:
                                while(True):
                                    wyb4 = input("choose position\n")
                                    if wyb4.isdigit() == True:
                                        wyb4 = int(wyb4) - 1
                                        break
                                if wyb4 > 8 or wyb4 < 0:
                                    print("position doesn't exist")
                                elif p_side[wyb4] != ["#","##","#"]:
                                    print("position is occupied")
                                else:
                                    power -= i[7]
                                    p_info[wyb4] = i
                                    if i[10] != 0:
                                        marksmen("p")
                                    if i[11] != 0:
                                        carrier("p")
                                    if i[9] != 0:
                                        t = 0
                                        for u in p_side2[wyb4]:
                                            if u == "#":
                                                p_side2[wyb4][t] = "t"
                                                p_side2[wyb4][t+1] = i[9]
                                                break
                                            t += 1
                                    if i[12] != 0:
                                        t = 0
                                        for u in p_side2[wyb4]:
                                            if u == "#":
                                                p_side2[wyb4][t] = "d"
                                                p_side2[wyb4][t+1] = "*"
                                                break
                                            t += 1
                                    if i[13] != 0:
                                        t = 0
                                        for u in p_side2[wyb4]:
                                            if u == "#":
                                                p_side2[wyb4][t] = "s"
                                                p_side2[wyb4][t+1] = "*"
                                                break
                                            t += 1
                                    if i[14] != 0:
                                        t = 0
                                        for u in p_side2[wyb4]:
                                            if u == "#":
                                                p_side2[wyb4][t] = "b"
                                                p_side2[wyb4][t+1] = "*"
                                                break
                                            t += 1
                                    if i[15] != 0:
                                        enchant("p",wyb4,i[15])
                                    if i[16] != 0:
                                        t = 0
                                        for u in p_side2[wyb4]:
                                            if u == "#":
                                                p_side2[wyb4][t] = "l"
                                                p_side2[wyb4][t+1] = "*"
                                                break
                                            t += 1
                                    if i[17] != 0:
                                        t = 0
                                        for u in p_side2[wyb4]:
                                            if u == "#":
                                                p_side2[wyb4][t] = "a"
                                                p_side2[wyb4][t+1] = i[17]
                                                break
                                            t += 1
                                    if i[18] != 0:
                                        t = 0
                                        for u in p_side2[wyb4]:
                                            if u == "#":
                                                p_side2[wyb4][t] = "c"
                                                p_side2[wyb4][t+1] = "*"
                                                break
                                            t += 1
                                    if i[19] != 0:
                                        anesthetize("p")
                                    if i[20] != 0:
                                        draw(i[20])
                                    p_side[wyb4][0] = i[5]
                                    p_side[wyb4][1] = i[4]
                                    p_side[wyb4][2] = i[6]
                                    for j in p_info[wyb4]:
                                        p_stats[wyb4].append(j)
                                    p_hand.remove(i)
                                    break
            attack("p",opp.health)
            if opp.health <= 0:
                print("your opponent is dead")
                level += 1
                spoils()
                fend()
                break
            for i in p_hand:
                p_discard.append(i)
            p_hand.clear()
            opp.move(ap)
            p_health = attack("o",p_health)
            if p_health <= 0:
                print("you are dead")
                break
            t = 0
            for i in ap:
                if i > 0:
                    ap[t] -= 1
                t += 1
    elif wyb == "S":
        c.execute("UPDATE players SET level=%s WHERE idplayers = %s", (level,id))
        conn.commit()
        c.execute("SELECT * FROM deck WHERE player_id = %s", id)
        wish = c.fetchall()
        for i in p_deck_add:
            s = 0
            for e in wish:
                if i[0] == e:
                    qua = e[2] + 1
                    c.execute("UPDATE deck SET quantity=%s WHERE player_id = %s AND card_id = %s", (qua,id,i[0]))
                    conn.commit()
                    s = 1
            if s == 0:
                c.execute("INSERT INTO deck(player_id,card_id,quantity) VALUES (%s,%s,%s)", (id,i[0],1))
                conn.commit()
        print("saved")
    elif wyb == "D":
        look(p_deck)
    elif wyb == "K":
        kdictonary()
    elif wyb == "+":
        spoils()
    elif wyb == "Q":
        break

