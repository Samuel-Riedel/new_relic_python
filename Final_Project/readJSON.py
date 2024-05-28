import json
file = "C:/Users/samue/OneDrive/Escritorio/Migracode/new_relic_python/Final_Project/testFile.json"


with open (file, "r") as json_file:
    data = json.load(json_file)
    name_data = (data["names"])
    print(data["names"])
    for i in name_data:
        name = (i["firstname"])
        age =(i["age"])
        print(f"{name} is {age}")




