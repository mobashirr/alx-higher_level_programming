#!/usr/bin/python3
import json


'''base class mod'''


class Base():
    '''base class'''

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return the JSON string representation of list_dictionaries'''
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        '''write the JSON string representation of list_objs to a file'''
        filename = cls.__name__ + '.json'
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        list_dicts_as_json = cls.to_json_string(list_dicts)

        with open(filename, 'w') as file:
            file.write(list_dicts_as_json)
    
    @staticmethod
    def from_json_string(json_string):
        '''return the list of the JSON string representation json_string'''
        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        dummy_instance = cls(1, 1) if cls.__name__ == 'Rectangle' else cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance