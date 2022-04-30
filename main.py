from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, NoTransition, CardTransition, SwapTransition, \
    FadeTransition, WipeTransition, FallOutTransition, RiseInTransition
from kivy.properties import StringProperty, NumericProperty, ObjectProperty
from kivy.core.audio import SoundLoader

game_won = False
game_over = False


class MainWidget(BoxLayout):
    Ennemy_img = StringProperty("images/slime.png")
    Effect_img = StringProperty("images/void.png")
    menu_widget = ObjectProperty()
    menu_size = NumericProperty(1)
    menu_size_x = NumericProperty(1)
    monster_hp_lost = NumericProperty(0)
    monster_hp = NumericProperty(100)
    monster_hp_left_ratio = NumericProperty(1)
    hero_hp_lost = NumericProperty(0)
    hero_hp = NumericProperty(100)
    hero_mp_lost = NumericProperty(0)
    hero_mp = NumericProperty(100)
    hp_left_ratio = NumericProperty(1)

    fizzle_sound = None
    game_over_sound = None
    sword_sound = None
    fire_sound = None
    wind_sound = None
    heal_sound = None
    victory_sound = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_audio()

    def init_audio(self):
        self.fizzle_sound = SoundLoader.load("audio/Fizzle.wav")
        self.sword_sound = SoundLoader.load("audio/sword.wav")
        self.fire_sound = SoundLoader.load("audio/fireball.wav")
        self.wind_sound = SoundLoader.load("audio/tornado.wav")
        self.heal_sound = SoundLoader.load("audio/healing.wav")
        self.victory_sound = SoundLoader.load("audio/victory.wav")
        self.game_over_sound = SoundLoader.load("audio/Game_over.wav")

        self.sword_sound.volume = 5
        self.fire_sound.volume = 3
        self.wind_sound.volume = 3
        self.heal_sound.volume = 5
        self.victory_sound.volume = 1
        self.game_over_sound.volume = 5

    def reset_all(self):
        self.Ennemy_img = "images/slime.png"
        self.Effect_img = "images/void.png"
        self.ids.Effect_spell.source = "images/void.png"
        self.menu_size = 1
        self.menu_size_x = 1
        self.monster_hp_lost = 0
        self.monster_hp = 100
        self.monster_hp_left_ratio = 1
        self.hero_hp_lost = 0
        self.hero_hp = 100
        self.hp_left_ratio = 1

    def spell_effect_reset(self):
        self.ids.Effect_spell.source = "images/void.png"

    def monster_turn(self):
        global game_won
        global game_over
        if self.monster_hp_lost >= self.monster_hp:
            self.victory_sound.play()
            game_won = True
            self.reset_all()
        if self.hero_hp_lost >= self.hero_hp:
            game_over = True
            self.reset_all()

    def on_spell_fire_pressed(self):
        mp_cost = 35
        if self.hero_mp - self.hero_mp_lost>= mp_cost:
            self.fire_sound.play()
            self.ids.Effect_spell.source = "images/fireball.png"
            self.monster_hp_lost += 30
            self.hero_mp_lost += 30
            # self.monster_hp_left_ratio = (self.monster_hp - self.hp_lost) / self.monster_hp
            self.monster_turn()
        else:
            self.fizzle_sound.play()

    def on_spell_wind_pressed(self):
        mp_cost = 20
        if self.hero_mp - self.hero_mp_lost >= mp_cost:
            self.wind_sound.play()
            self.ids.Effect_spell.source = "images/tornado.png"
            self.hero_hp_lost += 20
            self.hero_mp_lost += 20
            self.monster_turn()
        else:
            self.fizzle_sound.play()

    def on_spell_heal_pressed(self):
        mp_cost = 20
        if self.hero_mp - self.hero_mp_lost >= mp_cost:
            self.heal_sound.play()
            self.ids.Effect_spell.source = "images/heal.png"
            self.hero_hp_lost -= 20
            self.hero_mp_lost += mp_cost
            self.monster_turn()
        else:
            self.fizzle_sound.play()


class AllScreen(Screen):

    def on_attack(self):
        self.sword_sound.play()
        self.ids.Effect_spell.source = "images/slash.png"

    def ennemy_killed(self):
        self.ids.Ennemy_img.source = "images/void.png"

    def change_screen(self, screen_to_go):
        self.manager.current = screen_to_go


class MenuFull(TabbedPanel):
    pass


class PlayerInfo(BoxLayout):
    pass


class MagicMenu(BoxLayout):
    pass


class MenuScreen(AllScreen):
    def reset_game_won(self):
        global game_won
        global game_over

        game_won = False
        game_over = False


class GameOverScreen(AllScreen):
    game_over_sound = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_audio()

    def init_audio(self):
        self.game_over_sound = SoundLoader.load("audio/Game_over.wav")

        self.game_over_sound.volume = 5

    def reset_game_over(self):
        global game_won
        global game_over

        game_won = False
        game_over = False


class FightScreen(AllScreen):

    def check_game_end(self):
        if game_won:
            self.manager.current = 'menu'
        elif game_over:
            self.manager.current = 'game_over'


class TryAgainButton(Button):
    pass


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
    pass

    def build(self):
        # Create the screen manager
        sm = ScreenManager(transition=NoTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(FightScreen(name='combat'))
        sm.add_widget(GameOverScreen(name='game_over'))

        return sm


MonsterFightApp().run()
