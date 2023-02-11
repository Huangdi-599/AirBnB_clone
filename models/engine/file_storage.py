""" This file imports code from json, datetime, and pathlib """
import json
from models.base_model import BaseModel


class FileStorage:
    """ FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ All method. Simply returns the dictionary """
        return FileStorage.__objects

    def new(self, obj):
        """ New method. Fills in our dictionary """
        FileStorage.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        """ Save method. Saves/serializes the dictionary to our JSON file """
        with open(FileStorage.__file_path, 'w') as f:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """ Reload method. Loads/deserializes the dictionary from
        our JSON file """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = {}
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split('.')
                    FileStorage.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass
