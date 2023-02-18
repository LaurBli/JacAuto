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

    def goto_mainMenu(self, instance):
        sm = self.manager
        sm.current = 'main_menu'


class MainMenuScreen(GridLayout, Screen):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        self.cols = 2
        # self.add_widget(Label(text='Main Menu'))
        btn = Button(text='NITRO', font_size=40)
        btn.bind(on_press=self.goto_calculatorNitro)
        self.add_widget(btn)
        btn = Button(text='Ambasade',font_size=40)
        btn.bind(on_press=self.goto_calculatorAmbasade)
        self.add_widget(btn)
        btn = Button(text='Mixte',font_size=40)
        btn.bind(on_press=self.goto_calculatorMixte)
        self.add_widget(btn)
        btn = Button(text='A.o.p/Coop',font_size=40)
        btn.bind(on_press=self.goto_calculatorAop)
        self.add_widget(btn)

    def goto_calculatorNitro(self, instance):
        sm = self.manager
        sm.current = 'calculator_Nitro'

    def goto_calculatorAmbasade(self, instance):
        sm = self.manager
        sm.current = 'calculator_Ambasade'
    def goto_calculatorMixte(self, instance):
        sm = self.manager
        sm.current = 'calculator_Mixte'

    def goto_calculatorAop(self, instance):
        sm = self.manager
        sm.current = 'calculator_Aop'


class CalculatorNitro(GridLayout, MainMenuButton):
    def __init__(self, **kwargs):
        super(CalculatorNitro, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='KM plecare:', font_size=40))
        self.kilometri_plecare = TextInput(multiline=False, font_size=40)
        self.add_widget(self.kilometri_plecare)
        self.add_widget(Label(text='KM sosire:', font_size=40))
        self.kilometri_sosire = TextInput(multiline=False, font_size=40)
        self.add_widget(self.kilometri_sosire)
        self.add_widget(Label(text='Total KM:', font_size=40))
        self.result = Label(text='', font_size=40)
        self.add_widget(self.result)
        self.add_widget(Label(text='București:', font_size=40))
        self.kilometri_bucuresti = Label(text='', font_size=40)
        self.add_widget(self.kilometri_bucuresti)
        self.add_widget(Label(text='Alte localități:', font_size=40))
        self.kilometri_alte_localitati = Label(text='', font_size=40)
        self.add_widget(self.kilometri_alte_localitati)
        self.add_widget(Label(text='Drumuri neamenajate:', font_size=40))
        self.drumuri_neamenajate = Label(text='', font_size=40)
        self.add_widget(self.drumuri_neamenajate)
        self.add_widget(Label(text='Patrulare:', font_size=40))
        self.patrulare = Label(text='', font_size=40)
        self.add_widget(self.patrulare)
        self.subtract = Button(text='Calculează', font_size=40, background_color=(0, 1, 0, 1))
        self.subtract.bind(on_press=self.calculate)
        self.add_widget(self.subtract)
        self.gotoMenu = Button(text='Meniu', font_size=40)
        self.gotoMenu.bind(on_press=self.goto_mainMenu)
        self.add_widget(self.gotoMenu)

    def calculate(self, instance):
        try:
            first = int(self.kilometri_plecare.text)
            second = int(self.kilometri_sosire.text)
            difference = second - first
            if difference > 0:
                self.result.text = str(difference)
                self.kilometri_bucuresti.text = str(40)
                self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text))
                self.drumuri_neamenajate.text = str(0)
                self.patrulare.text = str(0)
            else:
                self.result.text = 'Iti da cu minus!'
                self.kilometri_bucuresti.text = ''
                self.kilometri_alte_localitati.text = ''
                self.drumuri_neamenajate.text = ''
                self.patrulare.text = ''
        except ValueError:
            self.result.text = 'Nu poti sa aduni litere!'
            self.kilometri_bucuresti.text = ''
            self.kilometri_alte_localitati.text = ''
            self.drumuri_neamenajate.text = ''
            self.patrulare.text = ''


class CalculatorAmbasade(GridLayout, MainMenuButton):
    def __init__(self, **kwargs):
        super(CalculatorAmbasade, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='KM plecare:', font_size=40))
        self.kilometri_plecare = TextInput(multiline=False, font_size=40)
        self.add_widget(self.kilometri_plecare)
        self.add_widget(Label(text='KM sosire:', font_size=40))
        self.kilometri_sosire = TextInput(multiline=False, font_size=40)
        self.add_widget(self.kilometri_sosire)
        self.add_widget(Label(text='Total KM:', font_size=40))
        self.result = Label(text='', font_size=40)
        self.add_widget(self.result)
        self.add_widget(Label(text='București:', font_size=40))
        self.kilometri_bucuresti = Label(text='', font_size=40)
        self.add_widget(self.kilometri_bucuresti)
        self.add_widget(Label(text='Alte localități:', font_size=40))
        self.kilometri_alte_localitati = Label(text='', font_size=40)
        self.add_widget(self.kilometri_alte_localitati)
        self.add_widget(Label(text='Drumuri neamenajate:', font_size=40))
        self.drumuri_neamenajate = Label(text='', font_size=40)
        self.add_widget(self.drumuri_neamenajate)
        self.add_widget(Label(text='Patrulare:', font_size=40))
        self.patrulare = Label(text='', font_size=40)
        self.add_widget(self.patrulare)
        self.subtract = Button(text='Calculează', font_size=40, background_color=(0, 1, 0, 1))
        self.subtract.bind(on_press=self.calculate)
        self.add_widget(self.subtract)
        self.gotoMenu = Button(text='Meniu', font_size=40)
        self.gotoMenu.bind(on_press=self.goto_mainMenu)
        self.add_widget(self.gotoMenu)

    def calculate(self, instance):
        try:
            first = int(self.kilometri_plecare.text)
            second = int(self.kilometri_sosire.text)
            difference = second - first
            if difference > 0:
                self.result.text = str(difference)
                self.kilometri_bucuresti.text = str(difference - 2)
                self.kilometri_alte_localitati.text = str(2)
                self.drumuri_neamenajate.text = str(0)
                self.patrulare.text = str(0)
            else:
                self.result.text = 'Iti da cu minus!'
                self.kilometri_bucuresti.text = ''
                self.kilometri_alte_localitati.text = ''
                self.drumuri_neamenajate.text = ''
                self.patrulare.text = ''
        except ValueError:
            self.result.text = 'Nu poti sa aduni litere!'
            self.kilometri_bucuresti.text = ''
            self.kilometri_alte_localitati.text = ''
            self.drumuri_neamenajate.text = ''
            self.patrulare.text = ''

class CalculatorMixte(GridLayout, MainMenuButton):

    def __init__(self, **kwargs):
        super(CalculatorMixte, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Kilometri plecare:',font_size =40))
        self.kilometri_plecare = TextInput(multiline=False, font_size =40)
        self.add_widget(self.kilometri_plecare)
        self.add_widget(Label(text='Kilometri sosire:',font_size =40))
        self.kilometri_sosire = TextInput(multiline=False, font_size =40)
        self.add_widget(self.kilometri_sosire)
        self.add_widget(Label(text='Total kilometri:',font_size =40))
        self.result = Label(text='',font_size =40)
        self.add_widget(self.result)
        self.add_widget(Label(text='Bucuresti:',font_size =40))
        self.kilometri_bucuresti = Label(text='', font_size =40)
        self.add_widget(self.kilometri_bucuresti)
        self.add_widget(Label(text='Alte localitati:',font_size =40))
        self.kilometri_alte_localitati = Label(text='', font_size =40)
        self.add_widget(self.kilometri_alte_localitati)
        self.add_widget(Label(text='Drumuri neamenajate:',font_size =40))
        self.drumuri_neamenajate = Label(text='', font_size =40)
        self.add_widget(self.drumuri_neamenajate)
        self.add_widget(Label(text='Patrulare:',font_size =40))
        self.patrulare = Label(text='', font_size =40)
        self.add_widget(self.patrulare)
        self.subtract = Button(text='Calculeaza',font_size =40, background_color=(0, 1, 0, 1))
        self.subtract.bind(on_press=self.calculate)
        self.add_widget(self.subtract)
        self.gotoMenu = Button(text='Meniu', font_size=40)
        self.gotoMenu.bind(on_press=self.goto_mainMenu)
        self.add_widget(self.gotoMenu)

    def calculate(self, instance):
        try:
            first = int(self.kilometri_plecare.text)
            second = int(self.kilometri_sosire.text)
            difference = second - first
            if difference > 0:
                self.result.text = str(difference)
                self.kilometri_bucuresti.text = str(3*(difference//4))
                self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text))
                self.drumuri_neamenajate.text = str(0)
                self.patrulare.text = str(0)
            else:
                self.result.text = 'Iti da cu minus!'
                self.kilometri_bucuresti.text = ''
                self.kilometri_alte_localitati.text = ''
                self.drumuri_neamenajate.text = ''
                self.patrulare.text = ''
        except ValueError:
            self.result.text = 'Nu poti sa aduni litere!'
            self.kilometri_bucuresti.text = ''
            self.kilometri_alte_localitati.text = ''
            self.drumuri_neamenajate.text = ''
            self.patrulare.text = ''


class CalculatorAsigurare(GridLayout,MainMenuButton):

    def __init__(self, **kwargs):
        super(CalculatorAsigurare, self).__init__(**kwargs)
        self.cols = 2
        self.dropdown = DropDown()
        options = ['Buftea', 'Bragadiru', 'Popești-Leordeni', 'Măgurele', 'Chitila', 'Otopeni', 'Voluntari', 'Pantelimon', 'Snagov']

        # add items to the dropdown
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=60, font_size=40, background_color=(1, 1, 0, 1))
            btn.bind(on_release=lambda buton: self.dropdown.select(buton.text))
            self.dropdown.add_widget(btn)

        # create a button to trigger the dropdown
        self.dropdown_btn = Button(text='Selecteaza zona', size_hint_y=None, size=(60, 60), font_size=40, background_color=(0, 1, 1, 1))
        self.dropdown_btn.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.dropdown_btn, 'text', x))

        # add the dropdown button to the main screen
        self.add_widget(self.dropdown_btn)
        # -------------------------------------------------NEW ONE
        self.dropdown2 = DropDown()
        options2 = ['Cu patrulare AUTO', 'Fara patrulare AUTO']

        # add items to the dropdown
        for option in options2:
            btn = Button(text=option, size_hint_y=None, height=60, font_size=40, background_color=(1, 1, 0, 1))
            btn.bind(on_release=lambda buton: self.dropdown2.select(buton.text))
            self.dropdown2.add_widget(btn)

        # create a button to trigger the dropdown
        self.dropdown2_btn = Button(text=' Tip patrulă', size_hint_y=None, size=(60, 60), font_size=40, background_color=(0, 1, 1, 1))
        self.dropdown2_btn.bind(on_release=self.dropdown2.open)
        self.dropdown2.bind(on_select=lambda instance, x: setattr(self.dropdown2_btn, 'text', x))

        # add the dropdown button to the main screen
        self.add_widget(self.dropdown2_btn)
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
        localitate = self.dropdown_btn.text
        if self.dropdown2_btn.text == 'Fara patrulare AUTO':

            if localitate == 'Buftea' or localitate == 'Chitila' or localitate == 'Bragadiru':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(15)
                        self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text))
                        self.drumuri_neamenajate.text = str(0)
                        self.patrulare.text = str(0)
                    else:
                        self.result.text = 'Iti da cu minus!'
                        self.kilometri_bucuresti.text = ''
                        self.kilometri_alte_localitati.text = ''
                        self.drumuri_neamenajate.text = ''
                        self.patrulare.text = ''
                except ValueError:
                    self.result.text = 'Nu poti sa aduni litere!'
                    self.kilometri_bucuresti.text = ''
                    self.kilometri_alte_localitati.text = ''
                    self.drumuri_neamenajate.text = ''
                    self.patrulare.text = ''
            elif localitate == 'Snagov' or localitate == 'Popești-Leordeni' or localitate == 'Otopeni':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(30)
                        self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text))
                        self.drumuri_neamenajate.text = str(0)
                        self.patrulare.text = str(0)
                    else:
                        self.result.text = 'Iti da cu minus!'
                        self.kilometri_bucuresti.text = ''
                        self.kilometri_alte_localitati.text = ''
                        self.drumuri_neamenajate.text = ''
                        self.patrulare.text = ''
                except ValueError:
                    self.result.text = 'Nu poti sa aduni litere!'
                    self.kilometri_bucuresti.text = ''
                    self.kilometri_alte_localitati.text = ''
                    self.drumuri_neamenajate.text = ''
                    self.patrulare.text = ''
            elif localitate == 'Pantelimon' or localitate == 'Voluntari':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(40)
                        self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text))
                        self.drumuri_neamenajate.text = str(0)
                        self.patrulare.text = str(0)
                    else:
                        self.result.text = 'Iti da cu minus!'
                        self.kilometri_bucuresti.text = ''
                        self.kilometri_alte_localitati.text = ''
                        self.drumuri_neamenajate.text = ''
                        self.patrulare.text = ''
                except ValueError:
                    self.result.text = 'Nu poti sa aduni litere!'
                    self.kilometri_bucuresti.text = ''
                    self.kilometri_alte_localitati.text = ''
                    self.drumuri_neamenajate.text = ''
                    self.patrulare.text = ''
            elif localitate == 'Măgurele':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(20)
                        self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text))
                        self.drumuri_neamenajate.text = str(0)
                        self.patrulare.text = str(0)
                    else:
                        self.result.text = 'Iti da cu minus!'
                        self.kilometri_bucuresti.text = ''
                        self.kilometri_alte_localitati.text = ''
                        self.drumuri_neamenajate.text = ''
                        self.patrulare.text = ''
                except ValueError:
                    self.result.text = 'Nu poti sa aduni litere!'
                    self.kilometri_bucuresti.text = ''
                    self.kilometri_alte_localitati.text = ''
                    self.drumuri_neamenajate.text = ''
                    self.patrulare.text = ''
            else:
                self.result.text = 'Selectează'
                self.kilometri_bucuresti.text = 'o'
                self.kilometri_alte_localitati.text = 'zonă!'
                self.drumuri_neamenajate.text = ''
                self.patrulare.text = ''
        elif self.dropdown2_btn.text == 'Cu patrulare AUTO':
            if localitate == 'Buftea' or localitate == 'Chitila' or localitate == 'Bragadiru':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.patrulare.text = str(random.randint(4, 10))
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(15)
                        self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text) - int(self.patrulare.text))
                        self.drumuri_neamenajate.text = str(0)

                    else:
                        self.result.text = 'Iti da cu minus!'
                        self.kilometri_bucuresti.text = ''
                        self.kilometri_alte_localitati.text = ''
                        self.drumuri_neamenajate.text = ''
                        self.patrulare.text = ''
                except ValueError:
                    self.result.text = 'Nu poti sa aduni litere!'
                    self.kilometri_bucuresti.text = ''
                    self.kilometri_alte_localitati.text = ''
                    self.drumuri_neamenajate.text = ''
                    self.patrulare.text = ''
            elif localitate == 'Snagov' or localitate == 'Popești-Leordeni' or localitate == 'Otopeni':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.patrulare.text = str(random.randint(4, 10))
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(30)
                        self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text) - int(self.patrulare.text))
                        self.drumuri_neamenajate.text = str(0)

                    else:
                        self.result.text = 'Iti da cu minus!'
                        self.kilometri_bucuresti.text = ''
                        self.kilometri_alte_localitati.text = ''
                        self.drumuri_neamenajate.text = ''
                        self.patrulare.text = ''
                except ValueError:
                    self.result.text = 'Nu poti sa aduni litere!'
                    self.kilometri_bucuresti.text = ''
                    self.kilometri_alte_localitati.text = ''
                    self.drumuri_neamenajate.text = ''
                    self.patrulare.text = ''
            elif localitate == 'Pantelimon' or localitate == 'Voluntari':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.patrulare.text = str(random.randint(4, 10))
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(40)
                        self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text) - int(self.patrulare.text))
                        self.drumuri_neamenajate.text = str(0)

                    else:
                        self.result.text = 'Iti da cu minus!'
                        self.kilometri_bucuresti.text = ''
                        self.kilometri_alte_localitati.text = ''
                        self.drumuri_neamenajate.text = ''
                        self.patrulare.text = ''
                except ValueError:
                    self.result.text = 'Nu poti sa aduni litere!'
                    self.kilometri_bucuresti.text = ''
                    self.kilometri_alte_localitati.text = ''
                    self.drumuri_neamenajate.text = ''
                    self.patrulare.text = ''
            elif localitate == 'Măgurele':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first

                    if difference > 0:
                        self.patrulare.text = str(random.randint(4, 10))
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(20)
                        self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text) - int(self.patrulare.text))
                        self.drumuri_neamenajate.text = str(0)

                    else:
                        self.result.text = 'Iti da cu minus!'
                        self.kilometri_bucuresti.text = ''
                        self.kilometri_alte_localitati.text = ''
                        self.drumuri_neamenajate.text = ''
                        self.patrulare.text = ''
                except ValueError:
                    self.result.text = 'Nu poti sa aduni litere!'
                    self.kilometri_bucuresti.text = ''
                    self.kilometri_alte_localitati.text = ''
                    self.drumuri_neamenajate.text = ''
                    self.patrulare.text = ''

            else:
                self.result.text = 'Selectează'
                self.kilometri_bucuresti.text = 'o'
                self.kilometri_alte_localitati.text = 'zonă!'
                self.drumuri_neamenajate.text = ''
                self.patrulare.text = ''
        else:
            self.result.text = 'Selectează'
            self.kilometri_bucuresti.text = 'tipul de '
            self.kilometri_alte_localitati.text = 'patrulă!'
            self.drumuri_neamenajate.text = ''
            self.patrulare.text = ''
class JacAuto(App):
    def build(self):
        sm = ScreenManager()
        main_menu = MainMenuScreen(name='main_menu')
        calculatorNitro = CalculatorNitro(name='calculator_Nitro')
        calculatorAmbasade = CalculatorAmbasade(name='calculator_Ambasade')
        calculatorMixte = CalculatorMixte(name='calculator_Mixte')
        calculatorAop = CalculatorAsigurare(name='calculator_Aop')
        sm.add_widget(main_menu)
        sm.add_widget(calculatorNitro)
        sm.add_widget(calculatorAmbasade)
        sm.add_widget(calculatorMixte)
        sm.add_widget(calculatorAop)
        return sm


if __name__ == '__main__':
    JacAuto().run()
