#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "file_storage.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split(".")
                    class_ = eval(class_name)
                    obj = class_(**obj_dict)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

