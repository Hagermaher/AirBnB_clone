#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, ob):
        """Adds new object to storage dictionary"""
        self.all().update({ob.to_dict()['__class__'] + '.' + ob.id: ob})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as fi:
            tmp = {}
            tmp.update(FileStorage.__objects)
            for ky, val in tmp.items():
                tmp[ky] = val.to_dict()
            json.dump(tmp, fi)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as fi:
                temp = json.load(fi)
                for ky, val in temp.items():
                        self.all()[ky] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
