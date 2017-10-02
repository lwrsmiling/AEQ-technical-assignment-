#!/usr/bin/python
# Transformation Autobots vs Deceptions


class Transformers(object):
    """docstring for Transformers"""
    def __init__(self, name, team, strength, intelligence, speed, endurance, rank, courage, firepower, skill):
        self.name = name
        self.team = team
        self.strength = strength
        self.intelligence = intelligence
        self.speed = speed
        self.endurance = endurance
        self.rank = rank
        self.courage = courage
        self.firepower = firepower
        self.skill = skill
    
    def get_overall_rating(self):  
        return self.strength + self.intelligence + self.speed + self.endurance + self.firepower

def compare(a, b):
    """docstring for Transformers"""
    if a.name == ('Optimus Prime' or 'Predaking') and b.name == ('Optimus Prime' or 'Predaking'):
        return 0
    elif a.name == ('Optimus Prime' or 'Predaking'):
        return 1
    elif b.name == ('Optimus Prime' or 'Predaking'):
        return -1
    elif a.courage - b.courage >= 4 and a.strength - b.strength >= 3:
        return 1
    elif b.courage - a.courage >= 4 and b.strength - a.strength >= 3:
        return -1
    elif a.courage - b.courage >= 3:
        return 1
    elif b.courage - a.courage >= 3:
        return -1
    else:
        return a.get_overall_rating() - b.get_overall_rating()

def main():
    USER_INPUT = [['Soundwave', 'D', 8, 9, 2, 6, 7, 5, 6, 10], \
                  ['Bluestreak', 'A', 6, 6, 7, 9, 5, 2, 9, 7], \
                  ['Hubcap', 'A', 4, 4, 4, 4, 4, 4, 4, 4]]

    autobots = []
    decepticons = []
    for transformer in USER_INPUT:
        if transformer[1] == 'D':
            decepticons.append(Transformers(*transformer))
        elif transformer[1] == 'A':
            autobots.append(Transformers(*transformer))

    decepticons.sort(key=lambda x: x.get_overall_rating(), reverse=True)
    autobots.sort(key=lambda x: x.get_overall_rating(), reverse=True)
    
    score_auto = 0
    score_dece = 0
    survivor_auto = []
    survivor_dece = []
    battle = 0
    opt_vs_pre = False
    while battle < len(decepticons) and battle < len(autobots):
        if autobots[battle].name == 'Optimus Prime' and decepticons[battle].name == 'Predaking':
            opt_vs_pre = True
            battle = battle + 1
            break
        elif compare(autobots[battle], decepticons[battle]) > 0:
            score_auto = score_auto + 1
            survivor_auto.append(autobots[battle].name)
        elif compare(autobots[battle], decepticons[battle]) < 0:
            score_dece = score_dece + 1
            survivor_dece.append(decepticons[battle].name)
        battle = battle + 1
    if not opt_vs_pre:
        survivor_auto = survivor_auto + [item.name for item in autobots[battle: len(autobots)]]
        survivor_dece = survivor_dece + [item.name for item in decepticons[battle: len(decepticons)]]
    print str(battle) + ' battle'
    if opt_vs_pre or score_auto == score_dece:
        print 'Winning team: No winner'
        print 'Survivors from the losing team: Not applicable'
    elif score_auto > score_dece:
        print 'Winning team: Autobots'
        print 'Survivors from the losing team: ' + survivor_dece[0]
    else:
        print 'Winning team: Decepticon'
        print 'Survivors from the losing team: ' + survivor_auto[0]

if __name__ == '__main__':
    main()