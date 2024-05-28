import json
file = "C:/Users/samue/OneDrive/Escritorio/Migracode/new_relic_python/Final_Project/testFile.json"


def write_json(data,filename="testFile.json"):
    with open (filename,"w") as f:
        json.dump(data,f,indent=4)

with open (file) as json_file:
    data = json.load(json_file)
    temp = data["names"]
    y = {"firstname":"testing", "age": 24}
    temp.append(y)



write_json(data,file)