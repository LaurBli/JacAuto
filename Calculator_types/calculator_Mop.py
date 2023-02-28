import random

from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.dropdown import DropDown
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyLabel(Label):
    def __init__(self, **kwargs):
        super(MyLabel, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0, 0, 1, 1)  # set the background color to red
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
class CalculatorMentinere(GridLayout):

    def __init__(self, **kwargs):
        super(CalculatorMentinere, self).__init__(**kwargs)
        self.cols = 2
        self.dropdown = DropDown()
        options = ['Buftea', 'Bragadiru', 'Popești-Leordeni', 'Măgurele', 'Chitila', 'Otopeni', 'Voluntari', 'Pantelimon', 'Snagov']

        # add items to the dropdown
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=60, font_size=40, background_color=(1, 1, 0, 1))
            btn.bind(on_release=lambda buton: self.dropdown.select(buton.text))
            self.dropdown.add_widget(btn)

        # create a button to trigger the dropdown
        self.dropdown_btn = Button(text='Selectează zona', size_hint_y=None, size=(60, 60), font_size=40, background_color=(0, 1, 1, 1))
        self.dropdown_btn.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.dropdown_btn, 'text', x))

        # add the dropdown button to the main screen
        self.add_widget(self.dropdown_btn)
        # -------------------------------------------------NEW ONE
        self.dropdown2 = DropDown()
        options2 = ['Doar M.o.p.', '+ alte misiuni']

        # add items to the dropdown
        for option in options2:
            btn = Button(text=option, size_hint_y=None, height=60, font_size=40, background_color=(1, 1, 0, 1))
            btn.bind(on_release=lambda buton: self.dropdown2.select(buton.text))
            self.dropdown2.add_widget(btn)

        # create a button to trigger the dropdown
        self.dropdown2_btn = Button(text=' Tip misiune', size_hint_y=None, size=(60, 60), font_size=40, background_color=(0, 1, 1, 1))
        self.dropdown2_btn.bind(on_release=self.dropdown2.open)
        self.dropdown2.bind(on_select=lambda instance, x: setattr(self.dropdown2_btn, 'text', x))

        # add the dropdown button to the main screen
        self.add_widget(self.dropdown2_btn)
        self.add_widget(MyLabel(text='Kilometri plecare:', font_size=40))
        self.kilometri_plecare = TextInput(multiline=False, font_size=40, input_type='number')
        self.add_widget(self.kilometri_plecare)
        self.add_widget(MyLabel(text='Kilometri sosire:', font_size=40))
        self.kilometri_sosire = TextInput(multiline=False, font_size=40, input_type='number')
        self.add_widget(self.kilometri_sosire)
        self.add_widget(Label(text='Total kilometri:', font_size=40))
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

    def calculate(self, instance):
        localitate = self.dropdown_btn.text
        if self.dropdown2_btn.text == 'Doar M.o.p.':

            if localitate == 'Buftea' or localitate == 'Chitila' or localitate == 'Bragadiru':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference >= 0:
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(15)
                        self.kilometri_alte_localitati.text = str(random.randint(3, 8))
                        self.drumuri_neamenajate.text = str(random.randint(10, 15))
                        self.patrulare.text = str(
                            difference - int(self.kilometri_bucuresti.text) - int(self.kilometri_alte_localitati.text) - int(self.drumuri_neamenajate.text))
                    else:
                        self.result.text = 'Iți dă cu minus!'
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
            elif localitate == 'Snagov':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(30)
                        self.kilometri_alte_localitati.text = str(random.randint(5, 20))
                        self.drumuri_neamenajate.text = str(random.randint(10, 25))
                        self.patrulare.text = str(
                            difference - int(self.kilometri_bucuresti.text) - int(self.kilometri_alte_localitati.text) - int(self.drumuri_neamenajate.text))
                    else:
                        self.result.text = 'Iți dă cu minus!'
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
            elif localitate == 'Popești-Leordeni' or localitate == 'Otopeni':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(30)
                        self.kilometri_alte_localitati.text = str(random.randint(3, 12))
                        self.drumuri_neamenajate.text = str(random.randint(5, 10))
                        self.patrulare.text = str(
                            difference - int(self.kilometri_bucuresti.text) - int(self.kilometri_alte_localitati.text) - int(self.drumuri_neamenajate.text))
                    else:
                        self.result.text = 'Iți dă cu minus!'
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
                        self.kilometri_alte_localitati.text = str(random.randint(3, 15))
                        self.drumuri_neamenajate.text = str(random.randint(10, 17))
                        self.patrulare.text = str(
                            difference - int(self.kilometri_bucuresti.text) - int(self.kilometri_alte_localitati.text) - int(self.drumuri_neamenajate.text))
                    else:
                        self.result.text = 'Iți dă cu minus!'
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
                        self.kilometri_alte_localitati.text = str(random.randint(3, 9))
                        self.drumuri_neamenajate.text = str(random.randint(10, 16))
                        self.patrulare.text = str(
                            difference - int(self.kilometri_bucuresti.text) - int(self.kilometri_alte_localitati.text) - int(self.drumuri_neamenajate.text))
                    else:
                        self.result.text = 'Iți dă cu minus!'
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
        elif self.dropdown2_btn.text == '+ alte misiuni':
            if localitate == 'Buftea' or localitate == 'Chitila' or localitate == 'Bragadiru':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(random.randint(15, 20))
                        self.kilometri_alte_localitati.text = str(random.randint(8, 18))
                        self.drumuri_neamenajate.text = str(random.randint(7, 13))
                        self.patrulare.text = str(
                            difference - int(self.kilometri_bucuresti.text) - int(self.kilometri_alte_localitati.text) - int(self.drumuri_neamenajate.text))

                    else:
                        self.result.text = 'Iți dă cu minus!'
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
            elif localitate == 'Snagov':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(random.randint(30, 40))
                        self.kilometri_alte_localitati.text = str(random.randint(10, 30))
                        self.drumuri_neamenajate.text = str(random.randint(10, 25))
                        self.patrulare.text = str(
                            difference - int(self.kilometri_bucuresti.text) - int(self.kilometri_alte_localitati.text) - int(self.drumuri_neamenajate.text))

                    else:
                        self.result.text = 'Iți dă cu minus!'
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
            elif localitate == 'Popești-Leordeni' or localitate == 'Otopeni':
                try:
                    first = int(self.kilometri_plecare.text)
                    second = int(self.kilometri_sosire.text)
                    difference = second - first
                    if difference > 0:
                        self.result.text = str(difference)
                        self.kilometri_bucuresti.text = str(random.randint(30, 35))
                        self.kilometri_alte_localitati.text = str(random.randint(6, 18))
                        self.drumuri_neamenajate.text = str(random.randint(5, 10))
                        self.patrulare.text = str(
                            difference - int(self.kilometri_bucuresti.text) - int(self.kilometri_alte_localitati.text) - int(self.drumuri_neamenajate.text))
                    else:
                        self.result.text = 'Iți dă cu minus!'
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
                        self.kilometri_bucuresti.text = str(random.randint(40, 45))
                        self.kilometri_alte_localitati.text = str(random.randint(7, 20))
                        self.drumuri_neamenajate.text = str(random.randint(8, 15))
                        self.patrulare.text = str(
                            difference - int(self.kilometri_bucuresti.text) - int(self.kilometri_alte_localitati.text) - int(self.drumuri_neamenajate.text))

                    else:
                        self.result.text = 'Iți dă cu minus!'
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
                        self.kilometri_bucuresti.text = str(random.randint(20, 28))
                        self.kilometri_alte_localitati.text = str(random.randint(6, 16))
                        self.drumuri_neamenajate.text = str(random.randint(8, 14))
                        self.patrulare.text = str(
                            difference - int(self.kilometri_bucuresti.text) - int(self.kilometri_alte_localitati.text) - int(self.drumuri_neamenajate.text))

                    else:
                        self.result.text = 'Iți dă cu minus!'
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
            self.kilometri_alte_localitati.text = 'misiune!'
            self.drumuri_neamenajate.text = ''
            self.patrulare.text = ''


class JacAutoApp(App):

    def build(self):
        return CalculatorMentinere()


if __name__ == '__main__':
    JacAutoApp().run()
