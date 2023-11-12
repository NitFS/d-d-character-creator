from kivy.metrics import dp
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix import label
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.anchorlayout import AnchorLayout

class Example(MDApp):
    data_tables = None

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"

        layout = MDFloatLayout()  
       
        button_box = MDBoxLayout(
            pos_hint={"center_x": 0.5},
            adaptive_size=True,
            padding="24dp",
            spacing="24dp",
        )

        button_py = MDBoxLayout(
            pos_hint={"center_x": 0.5},
            adaptive_size=True,
            padding="24dp",
            spacing="24dp",
            
        )
        
        for button_reg in ['Add character']:
            button_box.add_widget(
                MDRaisedButton(
                    text=button_reg, on_release=self.on_button_press

                )
            )

            
        
        for button_text in ["Remove character"]:
            button_box.add_widget(
                MDRaisedButton(
                    text=button_text, on_release=self.on_button_press
                )
            )

       
        
        self.data_tables = MDDataTable(
            pos_hint={"center_y": 0.5, "center_x": 0.5},
            size_hint=(0.9, 0.6),
            
            use_pagination=False,
            column_data=[
                ("Имя", dp(30)),
                ("Раса", dp(40)),
                ("Класс", dp(40)),
                ("Уровень", dp(40)),
            ],
            row_data=[('Валера','Клоун','11-3',-99)],
        )
        
        layout.add_widget(self.data_tables)
        layout.add_widget(button_box)

        return layout

    def on_button_press(self, instance_button: MDRaisedButton) -> None:
       

        try:
            {
                "Add character": self.add_row,
                "Remove character": self.remove_row,
            }[instance_button.text]()
        except KeyError:
            pass

    def add_row(self) -> None:
        last_num_row = int(self.data_tables.row_data[-1][0])
        self.data_tables.add_row()

    def remove_row(self) -> None:
        if len(self.data_tables.row_data) > 1:
            self.data_tables.remove_row(self.data_tables.row_data[-1])


Example().run()