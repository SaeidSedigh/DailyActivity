from datetime import datetime 
import os 
print(os.environ["DA_LINGO"])

__all__=(
    'OpenPropertyFile',
    'GetDateFormatted',
    'WritePropertyFile'
)
#for reading .properties file.
def OpenPropertyFile(file_path):
    data = {}
    with open(file_path + ".properties", 'r') as file: 
        lines = file.readlines()
        for line in lines: 
            key, value = line.strip().replace('"', '').split(':') 
            data[key.strip()] = value.strip() 
    return data
#for writing into .properties file.
def WritePropertyFile(file_path, data):
    with open(file_path, 'w') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n") 

def GetDateFormatted(dtObj,_ulang):
    ...

def ConvertToPersianWeekDay(dateobj):
	dayOfWeekNum = dateobj.weekday()
	return ["",
	 "TXT_monday",#monday
	 'TXT_tuesday',#tuesday
	 'TXT_wensday',#wensday
	 'TXT_thursday',#Thursday
	 'TXT_friday',#friday
	 'TXT_saturday',#Saturday
	 'TXT_sunday'#sunday
	 ][dayOfWeekNum]

def gregorian_to_jalali(gy, gm, gd): 
    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] 
    jy = 0 if gy <= 1600 else 979 
    gy -= 621 if gy <= 1600 else 1600 
    gy2 = gy + 1 if gm > 2 else gy 
    days = 365 * gy + (gy2 + 3) // 4 - (gy2 + 99) // 100 + (gy2 + 399) // 400 - 80 + gd + g_d_m[gm - 1] 
    jy += 33 * (days // 12053) 
    days %= 12053 
    jy += 4 * (days // 1461) 
    days %= 1461 
    jy += (days - 1) // 365 
    if days > 365: 
        days = (days - 1) % 365 
    jm = 1 + days // 31 if days < 186 else 7 + (days - 186) // 30 
    jd = 1 + (days % 31) if days < 186 else (days - 186) % 30 
 
    return {"year": jy, "month": jm, "day": jd} 
 
# Usage example 
result = gregorian_to_jalali(2002, 7, 1) 
print(result) 
 