from dataaccess import db

# Define the abstract base class M_BaseData
class M_BaseData():
    Id=0
    def __init__(self,cols):
        self.ColumnList = cols
    def Columns(self):
        columns = ', '.join(self.ColumnList)
        return columns;
    def Values(self):
        values = [getattr(self, col) for col in self.ColumnList]
        return values

# Implement a model class for DailyItem based on M_BaseData abstraction
class DailyItem(M_BaseData):
    TableName = 'DailyItem'
    Cols = ['Title', 'InputType']
    def __init__(self,title:str, input_type:int , Id=0):
        super().__init__(DailyItem.Cols)
        self.Id = Id
        self.Title = title
        self.InputType = input_type
        

def B_InsertDailyItem(m):
    placeholders = ', '.join(['?'] * len(m.ColumnList))
    query = f"INSERT INTO {m.TableName} ({m.Columns()}) VALUES ({placeholders})"
    record = db.Insert(query,m)
    return record;

def B_GetDailyItem(Id):
    record = db.GetOneRecord(f"SELECT Id, {', '.join(DailyItem.Cols)} FROM {DailyItem.TableName} WHERE Id = ?",(Id,))
    return record

def B_UpdateDailyItem(Id,m):
    set_values = [f"{col} = ?" for col in m.ColumnList]
    values = list(m.Values()) #tuple
    values.append(Id)

    query = f"UPDATE {m.TableName} SET {', '.join(set_values)} WHERE Id = ?"
    
    result = db.CommitWithParameter(query, tuple(values))
    return result;


#record = B_DailyItemInsert(DailyItem(0,"title5",1))

print(record)