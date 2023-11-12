class Charecter():
    
    def __init__(self, name, race, clas):
        self.name = name
        self.race = race
        self.clas = clas
        self.mainscor = [0,0,0,0,0,0]  #сила, ловкость, телосложение, инт, мудрость, харизма
        self.selfthrow = [0,0,0,0,0,0] #сила, ловкость, телосложение, инт, мудрость, харизма
        self.mhp = 0
        self.cd = 10
        self.skil = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
        self.masterbonus = 2
        self.scores = dict(
         воин = dict(startScore = [3,2,2,-1,0,1], bestScore = [0,2], startMaxHp = 10, bonusskil = [0,8,9,11,14]),
         паладин = dict(startScore = [1,0,2,-1,3,2], bestScore = [4,5], startMaxHp = 10, bonusskil = [7,17]),
         лучник = dict(startScore = [2,3,1,-1,2,0], bestScore = [0,1], startMaxHp = 10, bonusskil = [4,10,13]),
         плут = dict(startScore = [-1,3,0,2,1,2], bestScore = [1,3], startMaxHp = 8, bonusskil = [4,2,16,3]),
         человек = dict(addscor = [1,1,1,1,1,1]),
         гном = dict(addscor = [0,0,0,2,0,0]),
         эльф = dict(addscor = [0,2,0,0,0,0]),
         полурослик = dict(addscor = [0,2,0,0,0,0])
         )
    def __str__(self):
        return (f'Имя: {self.name}\n '
                f'Раса:{self.race}\n '
                f'Класс: {self.clas}\n'
                f'ХП: {self.mhp}\n'
                'Навыки:\n'
                f'атлетика: {self.skil[0]}\n'
                f'акробатика: {self.skil[1]}\n'
                f'ловкость рук: {self.skil[2]}\n'
                f'скрытность: {self.skil[3]}\n'
                f'анализ: {self.skil[4]}\n'
                f'история: {self.skil[5]}\n'
                f'магия: {self.skil[6]}\n'
                f'природа: {self.skil[7]}\n'
                f'религия: {self.skil[8]}\n'
                f'восприятие: {self.skil[9]}\n'
                f'выживание: {self.skil[10]}\n'
                f'медицина: {self.skil[11]}\n'
                f'проницательность: {self.skil[12]}\n'
                f'уход за животными: {self.skil[13]}\n'
                f'выступление: {self.skil[14]}\n'
                f'запугивание: {self.skil[15]}\n'
                f'обман: {self.skil[16]}\n'
                f'убеждение: {self.skil[17]}')
#генерит основные характеристики
    def mainscorreset(self):
        for i in range(6):
            self.mainscor[i] = self.scores[self.clas]['startScore'][i] + self.scores[self.race]['addscor'][i]
        return self.mainscor
#генерит спасброски
    def selfthrowgen(self):
        for i in range(6):
            self.selfthrow[i] = self.mainscor[i]
        self.selfthrow[self.scores[self.clas]['bestScore'][0]] = self.selfthrow[self.scores[self.clas]['bestScore'][0]] + self.masterbonus
        self.selfthrow[self.scores[self.clas]['bestScore'][1]] = self.selfthrow[self.scores[self.clas]['bestScore'][1]] + self.masterbonus
        return self.selfthrow
#генерируем очки здоровья
    def mheltpoint(self):
        self.mhp = self.scores[self.clas]['startMaxHp'] + self.mainscor[2]
        return self.mhp
#генерируем навыки
    def skils(self):
        self.skil[0] = self.mainscor[0] #сила: атлетика 
        for i in range(3):
            self.skil[i+1] = self.mainscor[1] #ловкость: акробатика, ловкость рук, скрытность
        for i in range(5):
            self.skil[i+4] = self.mainscor[3] #интеллект: анализ, история, магия, природа, религия
        for i in range(4):
            self.skil[i+9] = self.mainscor[4] #мудрость: восприятие, выживание, медицина, проницательность, уход за животными
        for i in range(4):
            self.skil[i+14] = self.mainscor[5] #харизма: выступление, запугивание, обман, убеждение

        for i in range(len(self.scores[self.clas]['bonusskil'])):
            self.skil[self.scores[self.clas]['bonusskil'][i]] = self.skil[self.scores[self.clas]['bonusskil'][i]] + self.masterbonus  
        return self.skil
#очки защиты
    def defscor(self):
        self.cd = self.cd + self.mainscor[1]
        return self.cd
    def generate(self):
        self.mainscorreset()
        self.selfthrowgen()
        self.mheltpoint()
        self.skils()
        self.defscor()
