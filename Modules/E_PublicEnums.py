class _e_item:
    Key=None
    Val=None
    Title = None
    def __init__(self,Key,Val,Name=''):
        self.Key=Key
        self.Val=Val
        self.Title=Name

class M_EnumOption:
    Enums:list=[] #list of _e_item
    def Get(self,val)->_e_item: #Get by value
        for i in self.Enums:
            if(i.Val == val):
                return i
    
    def _add(self,eobj):
        self.Enums.append(eobj)
    
    def __getitem__(self, key): #Get by key
        for item in self.Enums: 
            if item.Key == key: 
                return item.Val 
        raise KeyError(f"Key '{key}' not found in Enums") 

    def __setitem__(self, key, value): 
        for item in self.Enums: 
            if item.Key == key: 
                item.Val = value 
                return 
        raise KeyError(f"Key '{key}' not found in Enums") 

E_System = M_EnumOption()
########### LANGUAGES OF PROGRAM
E_System._add(_e_item(
    Key="RussianLanguage" , Val = 1 , Name="Russian"
))
E_System._add(_e_item(
    Key="PersianLanguage" , Val = 2 , Name="Persian"
))
E_System._add(_e_item(
    Key="EnglishLanguage" , Val = 3 , Name="English"
))
