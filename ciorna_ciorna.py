from kivy.app import App
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
        btn = Button(text='Ambasade')
        btn.bind(on_press=self.goto_calculatorAmbasade)
        self.add_widget(btn)
        btn = Button(text='Mixte')
        btn.bind(on_press=self.goto_calculatorMixte)
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
class MainMenuApp(App):
    def build(self):
        sm = ScreenManager()
        main_menu = MainMenuScreen(name='main_menu')
        calculatorNitro = CalculatorNitro(name='calculator_Nitro')
        calculatorAmbasade = CalculatorAmbasade(name='calculator_Ambasade')
        calculatorMixte = CalculatorMixte(name='calculator_Mixte')
        sm.add_widget(main_menu)
        sm.add_widget(calculatorNitro)
        sm.add_widget(calculatorAmbasade)
        sm.add_widget(calculatorMixte)
        return sm


if __name__ == '__main__':
    MainMenuApp().run()
