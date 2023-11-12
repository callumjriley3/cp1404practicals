"""
Dynamic Labels
CP1404 Practical 8
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Create dynamic labels for each element in a list."""

    def __init__(self, **kwargs):
        """Construct an app."""
        super().__init__(**kwargs)
        self.names = ['John', 'Maria', 'Sam', 'Bob', 'Jack']

    def build(self):
        """Build the Kivy GUI from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add to GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
