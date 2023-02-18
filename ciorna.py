import random

from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainMenuButton(Screen):
    def __init__(self, **kwargs):
        super(MainMenuButton, self).__init__(**kwargs)
    def goto_mainMenu(self,instance):
        sm = self.manager
        sm.current = 'main_menu'
class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        self.add_widget(Label(text='Main Menu'))
        btn = Button(text='NITRO',font_size=40)
        btn.bind(on_press=self.goto_calculator)
        self.add_widget(btn)

    def goto_calculator(self, instance):
        sm = self.manager
        sm.current = 'calculator'

class CalculatorScreen(GridLayout,MainMenuButton):
    def __init__(self, **kwargs):
        super(CalculatorScreen, self).__init__(**kwargs)
        self.cols = 2
        self.cols_minimum = {0: 300, 1: 100}
        # DROPDOWN INCEPE AICI------------------------------------------------------------------------------
        self.dropdown = DropDown()
        options = ['Buftea', 'Bragadiru', 'Popești-Leordeni', 'Măgurele', 'Chitila', 'Otopeni', 'Voluntari', 'Pantelimon', 'Snagov']

        # add items to the dropdown
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=60,font_size=40,background_color=(1, 1, 0, 1))
            btn.bind(on_release=lambda buton: self.dropdown.select(buton.text))
            self.dropdown.add_widget(btn)

        # create a button to trigger the dropdown
        self.dropdown_btn = Button(text='Selecteaza zona', size_hint_y=None,size =(60,60),font_size=40,background_color=(0, 1, 1, 1))
        self.dropdown_btn.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.dropdown_btn, 'text', x))

        # add the dropdown button to the main screen
        self.add_widget(self.dropdown_btn)
        self.add_widget(Label(text='', font_size=20,size_hint_y=None, height=44))
        self.add_widget(Label(text='Kilometri plecare:', font_size=40))
        self.kilometri_plecare = TextInput(multiline=False, font_size=40)
        self.add_widget(self.kilometri_plecare)
        self.add_widget(Label(text='Kilometri sosire:', font_size=40))
        self.kilometri_sosire = TextInput(multiline=False, font_size=40)
        self.add_widget(self.kilometri_sosire)
        self.add_widget(Label(text='Total kilometri:', font_size=40))
        self.result = Label(text='', font_size=40)
        self.add_widget(self.result)
        self.add_widget(Label(text='Bucuresti:', font_size=40))
        self.kilometri_bucuresti = Label(text='', font_size=40)
        self.add_widget(self.kilometri_bucuresti)
        self.add_widget(Label(text='Alte localitati:', font_size=40))
        self.kilometri_alte_localitati = Label(text='', font_size=40)
        self.add_widget(self.kilometri_alte_localitati)
        self.add_widget(Label(text='Drumuri neamenajate:', font_size=40))
        self.drumuri_neamenajate = Label(text='', font_size=40)
        self.add_widget(self.drumuri_neamenajate)
        self.add_widget(Label(text='Patrulare:', font_size=40))
        self.patrulare = Label(text='', font_size=40)
        self.add_widget(self.patrulare)
        self.subtract = Button(text='Calculeaza', font_size=40)
        self.subtract.bind(on_press=self.calculate)
        self.add_widget(self.subtract)
        self.gotoMenu = Button(text='Meniu', font_size=40)
        self.gotoMenu.bind(on_press=self.goto_mainMenu)
        self.add_widget(self.gotoMenu)

    def calculate(self, instance):
        if self.dropdown_btn.text == 'Buftea':
            self.result.text = 'CEAU'
        else:
            try:
                first = int(self.kilometri_plecare.text)
                second = int(self.kilometri_sosire.text)
                difference = second - first
                if difference > 0:
                    self.result.text = str(difference)
                    self.kilometri_bucuresti.text = str(difference // 4)
                    self.kilometri_alte_localitati.text = str(difference // 4)
                    self.drumuri_neamenajate.text = str(difference // 4)
                    self.patrulare.text = str(difference - (difference // 4) * 3)
                else:
                    self.result.text = 'Iti da cu minus!'
            except ValueError:
                self.result.text = 'Nu poti sa aduni litere!'
                self.kilometri_bucuresti.text = ''
                self.kilometri_alte_localitati.text = ''
                self.drumuri_neamenajate.text = ''
                self.patrulare.text = ''

class MainMenuApp(App):
    def build(self):
        sm = ScreenManager()
        main_menu = MainMenuScreen(name='main_menu')
        calculator = CalculatorScreen(name='calculator')
        sm.add_widget(main_menu)
        sm.add_widget(calculator)
        return sm

if __name__ == '__main__':
    MainMenuApp().run()
