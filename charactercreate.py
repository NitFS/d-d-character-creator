from kivy.uix.button import Button
from kivy.core.window import Window

from kivy.uix.recycleview import RecycleView
from kivy.uix.label import Label

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

from character import Charecter
from fileWorker import FileWorker


class CharacterCreatorApp(App):

    def __init__(self, charList, **kwargs):
        super(CharacterCreatorApp, self).__init__(**kwargs)
        self.charList = charList
        self.layout = BoxLayout(orientation = 'vertical', padding = 100, spacing = 5)

    def build(self):
        layout2 = BoxLayout(orientation = 'horizontal', padding = 10, spacing = 10)
       
        Window.clearcolor = (.07, .07, .07, 0.092458)

        self.list_data = self.charList

        # # Создаем виджет RecycleView с элементами из списка
        # self.rv = RecycleView(size_hint=(None, None), pos = {20,10})
        # self.rv.data = self.list_data
        # self.rv.viewclass = 'Label'
        # self.rv.fbind('on_scroll_stop', self.scroll_stopped)

        # # Связываем Label для отображения текста внутри RecycleView
        # self.rv.label_template = Label()

        self.character_name_input = TextInput(
            hint_text='Введите имя персонажа',
            size_hint_y = None,
            font_size=18,
            height = 50,
             background_color= (10, 10, 11, 0.043956456256231122546223778933333896594568945618416584561),
            multiline=False,
            foreground_color = (1, 1, 1, 1.90)
        )
        
        

        self.class_dropdown1 = DropDown()
        ras = ['Человек', 'Гном', 'Эльф', 'Полурослик']
        for char_class in ras:
            btn = Button(
                         text=char_class, 
                         size_hint_y=None, 
                         height=30,
                         background_color = (198,  2, 0, 0.89788465879 ),
                         color = (0,0,0,1))
            btn.bind(on_release=lambda btn: self.class_dropdown1.select(btn.text))
            self.class_dropdown1.add_widget(btn)

        self.class_button1 = Button(
            text='Выберите расу',
            size_hint=(None, None),
            
            width=150,
            height=44,
            background_color = (198,  2, 0, 0.89788465879 ),
            color = (0,0,0,1)
        )
        self.class_button1.bind(on_release=self.class_dropdown1.open)
        self.class_dropdown1.bind(on_select=lambda instance, x: setattr(self.class_button1, 'text', x))

        
        
        
        self.class_dropdown = DropDown()
        classes = ['Воин', 'Паладин', 'Лучник', 'Плут']
        for char_class in classes:
            btn = Button(
                         text=char_class,
                         size_hint_y=None,
                         height=30,pos =(100, 100),
                         background_color = (198,  2, 0, 0.89788465879 ),
                         color = (0,0,0,1)
                         )
            btn.bind(on_release=lambda btn: self.class_dropdown.select(btn.text))
            self.class_dropdown.add_widget(btn)

        self.class_button = Button(
            text='Выберите класс',
            size_hint=(None, None),
            background_color = (198,  2, 0, 0.89788465879 ),
            width=150,
            height=44,
            color = (0,0,0,1)
        )
        self.class_button.bind(on_release=self.class_dropdown.open)
        self.class_dropdown.bind(on_select=lambda instance, x: setattr(self.class_button, 'text', x))
        
        

        create_button = Button(
            text='Создать персонажа',
            size_hint=(None, None),
            width=170,
            height=44,
            background_color = (198,  2, 0, 0.89788465879 ),
            color = (0,0,0,1)
        )
        create_button.bind(on_press=self.create_character)
        
        self.character_xar = TextInput(
            hint_text='',
            size_hint_y = None,
            font_size=18,
             background_color= (10, 10, 11, 0.043956456256231122546223778933333896594568945618416584561),
            height = 600,
            foreground_color = (1, 1, 1, 1.90)
        
        )
        
        # layout2.add_widget(self.rv)
        layout2.add_widget(self.character_name_input) 
        layout2.add_widget(self.class_button1)
        layout2.add_widget(self.class_button)
        layout2.add_widget(create_button)
        self.layout.add_widget(self.character_xar)
        self.layout.add_widget(layout2)
        
        #layout2.add_widget(self.character_xar)
        
    

        return self.layout    

    # def scroll_stopped(self, rv, value):
    #     print(f"Scrolled to {value}")
        
    def create_character(self, instance):
        character_name = self.character_name_input.text
        character_class = self.class_button.text
        character_ras = self.class_button1.text
        char_xar = self.character_xar.text
        self.root.remove_widget(self.character_name_input)
        self.root.remove_widget(self.class_button1)
        self.root.remove_widget(self.class_button)
        if character_name and character_class and character_ras!= 'Выберите класс':
            print(f"Персонаж {character_name} создан! Класс: {character_class}! Раса:{character_ras}!")
            char = Charecter(name = character_name, clas = character_class.lower(), race=character_ras.lower())
            char.generate()
            fw = FileWorker(char)
            fw.write_to_file()
            self.character_xar.text = char.__str__()
        else:
            print("Введите имя персонажа и выберите класс.")