from kivy.app import App
from kivy.lang import Builder

class AnchorLayoutDemoApp(App):
    """Demo of AnchorLayout"""
    def build(self):
        """Build the kivy app from the kv file."""
        self.title = 'Anchor Layout Demo'
        self.root = Builder.load_file("anchor_layout.kv")
        return self.root
# Create and start the app running
AnchorLayoutDemoApp().run()