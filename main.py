from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition, CardTransition, SwapTransition, \
    FadeTransition, WipeTransition, FallOutTransition, RiseInTransition
from kivy.properties import StringProperty, NumericProperty, ObjectProperty


class MainWidget(BoxLayout):
    menu_widget = ObjectProperty()
    menu_size = NumericProperty(1)
    menu_size_x = NumericProperty(1)


class AllScreen(Screen):
    Ennemy_img = StringProperty("images/slime.png")
    Effect_img = StringProperty("images/void.png")

    def on_spell_pressed(self):
        self.ids.Effect_spell.source = "images/fireball.png"


class MenuScreen(AllScreen):
    pass


class MagicScreen(AllScreen):
    pass


class MenuPlayer(BoxLayout):

    def hide(self):
        self.size_hint_y = 0
        self.size_hint_x = 0


class AttacksButton(Button):
    text = "Attaques"


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


class MonsterFightApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(MagicScreen(name='magic'))

        return sm


MonsterFightApp().run()
