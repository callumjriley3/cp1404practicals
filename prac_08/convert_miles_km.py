"""
Miles to Kilometres Converter
CP1404 Practical 8
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

CONVERSION_RATE = 1.60934


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
            result = float(value) * CONVERSION_RATE
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = str(0.0)

    def handle_increment(self, text, increment_amount):
        """Handle incrementation of value in text box based on amount passed in."""
        value = self.convert_to_float(text) + increment_amount
        self.root.ids.input_number.text = str(value)

    @staticmethod
    def convert_to_float(text):
        """Convert text to float, returning 0.0 in case of error."""
        try:
            return float(text)
        except ValueError:
            return 0.0


ConvertMilesKilometresApp().run()
