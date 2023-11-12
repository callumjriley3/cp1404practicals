"""
Miles to Kilometres Converter
CP1404 Practical 8
"""


from kivy.app import App
from kivy.lang import Builder


class ConvertMilesKilometresApp(App):
    """ConvertMilesKilometresApp is a Kivy app for converting from miles to kilometres."""

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesKilometresApp().run()
