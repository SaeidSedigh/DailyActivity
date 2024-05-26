from Modules.E_PublicEnums import E_System

class Language_Manager:
    LangData:dict
    langFiles={
        E_System["RussianLanguage"] : f"{os.environ["DA_LINGO"]}/Russian",
        E_System["EnglishLanguage"] : f"{os.environ["DA_LINGO"]}/English",
        E_System["PersianLanguage"] : f"{os.environ["DA_LINGO"]}/Persian"
    }
    def __getitem__(self, key):
        return self.LangData[key]
    
    def Update_Text(self,lng:E_System):
        self.LangData = OpenPropertyFile(self.langFiles[lng])
   