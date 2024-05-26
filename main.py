#kivy.require("2.2.0")
import os
import sys
from pathlib import Path

import kivy
from kivy.lang import Builder
from kivy.clock import Clock 
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.modalview import ModalView

from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.theming import ThemeManager

if getattr(sys, "frozen", False):
    os.environ["DA_ROOT"] = sys._MEIPASS
else:
    sys.path.append(os.path.abspath(__file__).split("demos")[0])
    os.environ["DA_ROOT"] = str(Path(__file__).parent)
os.environ["DA_ASSETS"] = os.path.join(
    os.environ["DA_ROOT"], f"assets{os.sep}"
)
os.environ["DA_LINGO"] = os.path.join(
    os.environ["DA_ROOT"], f"InterfaceLanguages{os.sep}"
)

from View.ManagerScreen.manager_screen import ManagerScreen
from View.MainScreen import MainScreen
from View.SettingsView import SettingsView
from InterfaceLanguages.LanguageManager import Language_Manager
from View.Components.SelectDialogBox import SelectDialog

from Modules.B_PublicFunction import *
from Modules.E_PublicEnums import E_System

Window.softinput_mode = "below_target"

class RootWidget(MDFloatLayout):
    pass

class DailyActivity(MDApp):
    ############## APP BOOTSTRAP
    Settings = {
        "Language"
    }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls = ThemeManager()
        self.theme_cls.theme_style = "Light"  # Choose Light or Dark theme
        self.theme_cls.primary_palette = "Indigo"  # Set primary color palette
        self.theme_cls.accent_palette = "Pink"  # Set accent color palette
        self.theme_cls.divider_color = "Red"
        self.theme_cls.font_styles.update({"H1": ["Roboto", 36, False, False]})
        #For loading dialog box
        self.LoadingBox = None
        #bootstraping settings
        self.LoadSavedSettings()
        self._changelangCallback(int(self.Settings['Language']))
    
    def LoadSavedSettings(self):
        result = {}
        result = OpenPropertyFile("Settings")
        self.Settings = result
    
    def SaveSettingsFile(self):
        WritePropertyFile("Settings",self.Settings)

    ############### LANGUAGE INTERFACE : 
    Resource = Language_Manager()
    def ChangeInterfaceLanguage(self): 
        for widget in self.root.walk(restrict=True):
            if hasattr(widget, 'text_key') and widget.text_key:
                try:
                    widget.text = self.Resource[widget.text_key]
                except KeyError:
                    widget.text = f"@@{widget.text_key}@@"
        self.LoadingBox.dismiss()
    def SetUserInterfaceLanguage(self,enumLanguage):
        self.Settings["Language"] = enumLanguage
        self.SaveSettingsFile()
        self.Resource.Update_Text(enumLanguage)
        Clock.schedule_once(lambda dt: self.ChangeInterfaceLanguage()) 
        return
    def _changelangCallback(self,newLang):
        self.OpenLoading()
        self.SetUserInterfaceLanguage(newLang)
    ###############
    ############### Settings page:
    
    _dialogLanguage = SelectDialog(title="App Language", description="Select the application language", options=[
        (E_System.Get(i).Title,"language",lambda x: self._changelangCallback(lng,lambda x: self._dialogLanguage.dismiss())) for i in Language_Manager.langFiles
    ])
    def 
    _dialogLanguage.open()

    def OpenLoading(self) -> None:
        if not self.LoadingBox:
            image = Image(
                source="assets/images/loading.gif",
                size_hint=(0.15, 0.15),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            self.LoadingBox = ModalView(
                background="assets/images/modal-bg.png",
            )
            self.LoadingBox.add_widget(image)
        self.LoadingBox.open()

    def build(self) -> ManagerScreen:
        #Load the KV string from the DailyActivity.kv file
        kv_stringLayout = Builder.load_file("DailyActivity.kv")
        #Load the KV string from the /MainScreen/MainScreen.kv file
        kv_stringMainPage = Builder.load_file("View/MainScreen/MainScreen.kv")
        #Load the KV string from the /SettingsView/SettingsView.kv file
        kv_stringMainPage = Builder.load_file("View/SettingsView/SettingsView.kv")

        # Create an instance of the RootWidget defined in the KV file
        self.root = RootWidget()
        
        # Add the ManagerScreen instance to the RootWidget
        # root.add_widget(self.manager_screen)
        
        return self.root

if __name__ == "__main__":
    DailyActivity().run()