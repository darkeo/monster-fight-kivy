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
from kivy.core.audio import SoundLoader


class MainWidget(BoxLayout):
    menu_widget = ObjectProperty()
    menu_size = NumericProperty(1)
    menu_size_x = NumericProperty(1)


class AllScreen(Screen):
    Ennemy_img = StringProperty("images/slime.png")
    Effect_img = StringProperty("images/void.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_audio()

    def on_attack(self):
        self.sword_sound.play()
        self.ids.Effect_spell.source = "images/slash.png"

    def spell_effect_reset(self):
        self.ids.Effect_spell.source = "images/void.png"

    def on_spell_fire_pressed(self):
        self.fire_sound.play()
        self.ids.Effect_spell.source = "images/fireball.png"

    def on_spell_wind_pressed(self):
        self.wind_sound.play()
        self.ids.Effect_spell.source = "images/tornado.png"

    def on_spell_heal_pressed(self):
        self.heal_sound.play()
        self.ids.Effect_spell.source = "images/heal.png"

    def ennemy_killed(self):
        self.ids.Ennemy_img.source = "images/void.png"

    sword_sound = None
    fire_sound = None
    wind_sound = None
    heal_sound = None

    def init_audio(self):
        self.sword_sound = SoundLoader.load("audio/sword.wav")
        self.fire_sound = SoundLoader.load("audio/fireball.wav")
        self.wind_sound = SoundLoader.load("audio/tornado.wav")
        self.heal_sound = SoundLoader.load("audio/healing.wav")

        self.sword_sound.volume = 5
        self.fire_sound.volume = 3
        self.wind_sound.volume = 3
        self.heal_sound.volume = 5


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
