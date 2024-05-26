from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog

class SelectDialog(MDDialog):
    def __init__(self, title, description="", options=None, **kwargs):
        super().__init__(title=title, **kwargs)
        self.description = description
        self.options = options if options else []
        self.box = MDBoxLayout(orientation='vertical', spacing='12dp')
        self._build_content()
        
    def _build_content(self):
        if self.description:
            self.box.add_widget(MDLabel(text=self.description, theme_text_color="Secondary"))
        for option in self.options:
            self.box.add_widget(self._create_button(option))
        self.type = 'custom'
        self.content_cls = self.box

    def _create_button(self, option):
        text, icon, callback = option
        button = MDRaisedButton(
            text=text,
            icon=icon,
            on_release=callback
        )
        return button
