# Status,Class,GEN,Power,Role,STRAG,STR,SPD,AGL,DUR,END,INT,ZCN,ZPO,STA,PER,VRT,ADP,BTOT,HP,ATT,DEF,RES,FCS,ACC,ZCP,HTOT,FTOT,TOT


# def suggest_tier(total):
#     if total == 108:    return "Perfect"
#     elif total >= 92:   return "Veteran"
#     elif total >= 55:   return "Amateur"
#     elif total >= 24:   return "Trained"
#     else:               return "Everyday"
# Clean progression that tells a story too:

# <= 23    Everyday   — just existing,no real ability
# 24-54    Trained    — put in work,limited results
# 55-91    Amateur    — real capability,not refined
# 92-107   Veteran    — seasoned,dangerous
# 108      Perfect    — theoretical ceiling,basically a myth

roles = ['block','catalyst','disruptor','flank','na','safety','scout','stringer','striker','summoner']

strag = ['agility','group','na','range','sparing','tactics']

classes = ['combat','na','service','utility']

stat_labels = ['STR','SPD','AGL','DUR','END','INT','ZCN','ZPO','STA','PER','VRT','ADP']
'''
str = 4
spd = 8
agl = 7
dur = 4
end = 2
int = 2
zcn = 4
zpo = 5
sta = 8
per = 4
vrt = 3
adp = 3
htot = str + spd + agl + dur + end + int + zcn + zpo + sta + per + vrt + adp

hp   = (dur + end + sta) * 8
att  = (str + spd + zcn + zpo) * 8
defc = (dur + end + adp) * 8
res  = (dur + sta + adp) *8
fcs  = (sta + per + adp) * 8
acc  = (int + zcn + per) * 8
zcp  = (hp + att + defc) * 10
btot = hp + att + defc + res + fcs + acc + zcp 


ftot = htot+btot
tot = htot+btot+ftot

print(htot)
print(btot)
print(ftot)
print(tot)
'''

import random
my_list = ['apple','banana','cherry']

# print(random.randint(0,9))
# print(random.choice(my_list))

rand_nums = []
for _ in range(12):
    n = random.randint(0,9)
    rand_nums.append(n)
# print(rand_nums)

print(f"Role  : {random.choice(roles)}")
print(f"STRAG : {random.choice(strag)}")
print(f"Class : {random.choice(classes)}")

stat_nums = random.choices(range(0,9),k=12)
# print(f"labels: {stat_labels}")
print(f"Stats : {stat_nums}")

stats = dict(zip(stat_labels,stat_nums))
print(f"Stats : {stats}")

HP  = (stats['DUR'] + stats['END'] + stats['STA']) * 8
ATT = (stats['STR'] + stats['SPD'] + stats['ZCN'] + stats['ZPO']) * 8
DEF = (stats['DUR'] + stats['END'] + stats['ADP']) * 8
RES = (stats['DUR'] + stats['STA'] + stats['ADP']) * 8
FCS = (stats['STA'] + stats['PER'] + stats['ADP']) * 8
ACC = (stats['INT'] + stats['ZCN'] + stats['PER']) * 8
ZCP = (HP  + ATT + DEF) * 10

BTOT = HP + ATT + DEF + RES + FCS + ACC + ZCP
print(HP)
print(ATT)
print(DEF)
print(ZCP)
# print(BTOT)

# id | role      | strag    | class   | stats                   |
# 1  | catalyst  | sparing  | na      | 3,4,5,2,8,7,1,1,5,4,5,8 |
# 2  | na        | agility  | service | 5,2,5,4,8,7,3,1,8,2,5,0 |
# 3  | striker   | na       | utility | 3,6,5,4,7,7,7,2,4,2,4,7 |
# 4  | disruptor | range    | utility | 4,8,3,2,5,0,1,1,2,3,6,5 |
# 5  | catalyst  | range    | na      | 4,3,6,2,8,3,8,5,8,5,3,5 |
# 6  | striker   | group    | combat  | 8,2,6,7,3,2,2,3,4,1,6,4 |
# 7  | disruptor |  agility | service | 1,8,0,0,5,4,4,1,5,7,4,8 |
# 8  | safety    |sparing   | service | 0,0,1,3,8,0,7,0,4,4,4,0 |
# 9  | flank     | tactics  | utility | 0,4,1,7,6,8,5,8,4,8,4,5 |
# 10 | safety    | agility  | service | 7,3,6,6,0,6,4,1,5,2,7,0 |
# 11 | flank     | agility  | service | 2,3,3,8,3,3,2,7,6,1,3,2 |