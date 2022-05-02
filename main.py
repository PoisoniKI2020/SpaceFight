__version__ = "Alpha 1.0"

from kivy.animation import Animation
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

Window.size = (540, 960)


class SpaceFightApp(App):
    def to_settings(self, btn):
        self.to_center.start(self.settings_menu)
        self.to_left_side.start(self.main_menu)

    def to_menu_from_settings(self, btn):
        self.to_right_side.start(self.settings_menu)
        self.to_center.start(self.main_menu)

    main = FloatLayout()

    def to_client(self, btn):
        self.to_center.start(self.settings_menu)
        self.to_left_side.start(self.main_menu)

    def to_menu_from_client(self, btn):
        self.to_right_side.start(self.settings_menu)
        self.to_center.start(self.main_menu)

    main = FloatLayout()
    main_menu = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(1, 1), pos_hint={'center_x': 0.5})
    settings_menu = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(1, 1),
                              pos_hint={'center_x': 1.5})
    client_menu = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(1, 1),
                            pos_hint={'center_x': 1.5})
    to_center = Animation(pos_hint={'center_x': 0.5}, duration=0.5)
    to_left_side = Animation(pos_hint={'center_x': -0.5}, duration=0.5)
    to_right_side = Animation(pos_hint={'center_x': 1.5}, duration=0.5)

    def build(self):
        self.main_menu.add_widget(Label(text="L0G0", font_size=60, size_hint=(1, 1.5), pos=(0.5, 0)))
        self.main_menu.add_widget(
            Button(text="Сервер", font_size=30, size_hint=(0.75, 0.5), pos_hint={'center_x': 0.5}))
        self.main_menu.add_widget(
            Button(text="Клиент", font_size=30, size_hint=(0.75, 0.5), pos_hint={'center_x': 0.5}))
        self.main_menu.add_widget(
            Button(text="Настройки", font_size=25, size_hint=(0.5, 0.3), pos_hint={'center_x': 0.5},
                   on_press=self.to_settings))
        self.settings_menu.add_widget(ColorPicker())
        self.settings_menu.add_widget(
            Button(pos=(0, 0), on_press=self.to_menu_from_settings, size_hint=(0.1, 0.1), text="Назад"))
        self.main.add_widget(self.main_menu)
        self.main.add_widget(self.settings_menu)
        Window.clearcolor = (0.6, 0.9, 1, 1)
        return self.main


if __name__ == "__main__":
    SpaceFightApp().run()
