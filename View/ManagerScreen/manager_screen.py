from kivy.uix.screenmanager import NoTransition
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager


class ManagerScreen(MDScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.transition = NoTransition()
        
    def SwitchScreenCallback(self, screen_name: str) -> None:
        self.current = screen_name