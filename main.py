from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty


class MainWidget(BoxLayout):
    pass

class AttacksButton(Button):
    text = "Attaques"
    def on_press(self):
        print("attaque")


class MagicButton(Button):
    text = "Magie"
    def on_press(self):
        print("Liste des Sorts")


class ObjectButton(Button):
    text = "Objets"
    def on_press(self):
        print("Liste des Objets")


class FleeButton(Button):
    text = "Fuite"
    def on_press(self):
        print("Fuite")


class MonsterFightApp(App):
    pass


MonsterFightApp().run()
