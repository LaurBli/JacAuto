from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class CalculatorNitro(GridLayout):

    def __init__(self, **kwargs):
        super(CalculatorNitro, self).__init__(**kwargs)
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
        self.subtract = Button(text='Calculeaza',font_size =40)
        self.subtract.bind(on_press=self.calculate)
        self.add_widget(self.subtract)

    def calculate(self, instance):
        try:
            first = int(self.kilometri_plecare.text)
            second = int(self.kilometri_sosire.text)
            difference = second - first
            if difference >0:
                self.result.text = str(difference)
                self.kilometri_bucuresti.text = str(40)
                self.kilometri_alte_localitati.text = str(difference - int(self.kilometri_bucuresti.text))
                self.drumuri_neamenajate.text = str(0)
                self.patrulare.text = str(0)
            else:
                self.result.text = 'Iti da cu minus!'
        except ValueError:
            self.result.text = 'Nu poti sa aduni litere!'
            self.kilometri_bucuresti.text = ''
            self.kilometri_alte_localitati.text = ''
            self.drumuri_neamenajate.text = ''
            self.patrulare.text = ''

class JacAutoApp(App):

    def build(self):
        return CalculatorNitro()

if __name__ == '__main__':
    JacAutoApp().run()