"""
Miles to Kilometres Converter
CP1404 Practical 8
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesKilometresApp(App):
    """ConvertMilesKilometresApp is a Kivy app for converting from miles to kilometres."""
    result = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self, value):
        """Handle conversion of value in miles to kilometres and output result to label."""
        try:
            result = float(value) * 1.60934
            self.root.ids.output_label.text = str(result)
        except ValueError:
            pass


ConvertMilesKilometresApp().run()
