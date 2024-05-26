from kivymd.uix.screen import MDScreen
from kivy.lang import Builder 



class SettingsView(MDScreen):
    def __init__(self,*args,**kwargs):
        super().__init__(**kwargs)
        self.HeaderTitle = "Settings"
    def show_language_dialog(self):
        options = [
            ("English", "language", lambda x: self.set_language("English")),
            ("Georgian", "language", lambda x: self.set_language("Georgian")),
        ]
        dialog = SelectDialog(title="App Language", description="Select the application language", options=options)
        dialog.open()

    def show_calendar_dialog(self):
        options = [
            ("Georgian", "calendar", lambda x: self.set_calendar("Georgian")),
            ("Gregorian", "calendar", lambda x: self.set_calendar("Gregorian")),
        ]
        dialog = SelectDialog(title="Calendar Setting", description="Select the calendar type", options=options)
        dialog.open()