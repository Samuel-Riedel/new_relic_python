import json

class Escribir():
    pass
    def escribir(data, filename="points.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

def append_data_to_file(file_path, new_data):
    with open(file_path) as json_file:
        data = json.load(json_file)
        temp = data["points"]
        temp.append(new_data)
    Escribir.escribir(data, file_path)

