import os
from os import path
import json
from character import Charecter

class FileWorker():

    def __init__(self, char = None):
        self.char = char
    
    def write_to_file(self):
        #Генерирует JSON для записи
        if self.char is None:
            #print("Иди заполни персонажа, куска дибил")
            return False
        charDict = {"title" : "CHARACTER", "name" : self.char.name, "race" : self.char.race,
         "clas" : self.char.clas, "mainscor" : self.char.mainscor, "selfthrow" : self.char.selfthrow,
         "mhp" : self.char.mhp, "cd" : self.char.cd, "skil" : self.char.skil, "masterbonus" : self.char.masterbonus}
        dmpdChar = json.dumps(charDict, ensure_ascii=False)

        #Создает файл персонажа, если его нет. Заполняет файл персонажа JSON строкой
        self.fp = open("chars/" + self.char.name + ".dnd", 'w+')
        self.fp.write(dmpdChar)
        self.fp.close()
        return True
    
    def read_from_file(self, charName):
        #Если char уже объявлен - перезапишет его статы на новые в объекте
        self.fp = open("chars/" + charName + ".dnd", "r+")
        tmp = self.fp.read()
        tmp = json.loads(tmp)

        #Запись полученных статов
        self.char = Charecter(name=tmp['name'],race=tmp['race'],clas=tmp['clas'])
        self.char.mainscore = tmp['mainscor']
        self.char.selfthrow = tmp['selfthrow']
        self.char.mhp = tmp['mhp']
        self.char.cd = tmp['cd']
        self.char.skil = tmp['skil']
        self.char.masterbonus = tmp['masterbonus']
        self.fp.close()
        return True

    def getCharList(self):
        files = []
        files += os.listdir("chars/")
        return files

# lol = Charecter(name='Debri', race='гном', clas='плут')
# lol.generate()
# fwLol = FileWorker(lol)
# fwLol.write_to_file()
# fwLol.getCharList()
# print(fwLol.char)
# fwLol.read_from_file("Romass")