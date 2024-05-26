def write_language_resource_file(file_name, language_data): 
    with open(file_name, 'a', encoding='utf-8') as file: 
        for key, value in language_data.items(): 
            file.write(f"{key}: '{value}'\n") 
 
# Get inputs for Russian language resources 
russian_data = {} 
print("Enter Russian language resources (text_key: text). Enter 'done' to finish.") 
while True: 
    input_text = input() 
    if input_text.lower() == 'done': 
        break 
    key, value = input_text.split(':') 
    russian_data[key.strip()] = value.strip() 
 
# Append Russian language resources to file 
write_language_resource_file('Russian.properties', russian_data) 
 
# Get inputs for English language resources 
english_data = {} 
print("Enter English language resources (text_key: text). Enter 'done' to finish.") 
while True: 
    input_text = input() 
    if input_text.lower() == 'done': 
        break 
    key, value = input_text.split(':') 
    english_data[key.strip()] = value.strip() 
 
# Append English language resources to file 
write_language_resource_file('English.properties', english_data) 
 
# Get inputs for Persian language resources 
persian_data = {} 
print("Enter Persian language resources (text_key: text). Enter 'done' to finish.") 
while True: 
    input_text = input() 
    if input_text.lower() == 'done': 
        break 
    key, value = input_text.split(':') 
    persian_data[key.strip()] = value.strip() 
 
# Append Persian language resources to file 
write_language_resource_file('Persian.properties', persian_data) 
 
print("Language resources have been appended to files.") 