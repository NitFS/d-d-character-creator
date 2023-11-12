from character import Charecter
from fileWorker import FileWorker
from charactercreate import CharacterCreatorApp


fw = FileWorker()

charList = fw.getCharList()

if __name__ == '__main__':
    CharacterCreatorApp(charList).run()

while flag:
# Если пользователь выбирает готового персонажа из charList, вызываешь read_from_file
# Если хочет создать персонажа, делаешь char = Charecter('имя','РАССА','КЛАСС') и char.generate()
# Сохранение персонажа на write_to_file, но нужно сделать fw = FileWorker(char)
# 
# 
#
    print("Pizdec")