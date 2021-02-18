#!/usr/bin/python3
"""The entry point to the HBnB console"""


import cmd
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    The HBNB Command Class
    ======================

    The class used to create and use all HBnB associated
    commands. Inherits from cmd.

    """

# Defaults

    def __init__(self):
        """initializes the HBNB command class"""
    # inits parent class attributes
        super(HBNBCommand, self).__init__()
    # sets CMD and HBNBCommand attributes
        self.prompt = "(hbnb) "

    # overrides default empty line behavior of repeating
    # last working command
    def emptyline(self):
        """repeats line on receiving empty line"""
        pass

    # enables exitability
    def can_exit(self):
        """enables exiting of the cmd loop"""
        return True

# All Support Commands:

    # Quit command to exit the program
    def do_quit(self, s):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, s):
        """Sends end of file to quit"""
        exit()

    def do_create(self, model_type="None"):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Ex: $ create BaseModel
        """
        if model_type == "" or None:
            print("** class name missing **")
        elif model_type not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        else:
            if model_type == "BaseModel":
                new_model = BaseModel()
            elif model_type == "State":
                new_model = State()
            elif model_type == "City":
                new_model = City()
            elif model_type == "User":
                new_model = User()
            elif model_type == "Place":
                new_model = Place()
            elif model_type == "Amenity":
                new_model = Amenity()
            elif model_type == "Review":
                new_model = Review()
            print(new_model.id)
            storage.new(new_model)
            storage.save()

    def do_show(self, model_key=None):
        """
        Prints the string representation of an instance
        based on the class name and id.

        Ex: $ show BaseModel 1234-1234-1234.
        """
        class_name = None
        model_id = None
        if model_key != "":
            try:
                class_name = model_key.split(" ")[0]
                model_id = model_key.split(" ")[1]
            except IndexError:
                pass
        if class_name is None:
            print("** class name missing **")
        elif class_name not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        elif model_id is None:
            print("** instance id missing **")
        else:
            model_key = class_name + "." + model_id
            key_exists = False
            for key in storage.all().keys():
                if key == model_key:
                        print(storage.all().get(key))
                        key_exists = True
                        break
            if key_exists is not True:
                print("** no instance found **")

    def do_destroy(self, model_key=None):
        """
        destroy: Deletes an instance based on the class name and id
        (save the change into the JSON file).

        Ex: $ destroy BaseModel 1234-1234-1234.
        """
        class_name = None
        model_id = None
        if model_key != "":
            try:
                class_name = model_key.split(" ")[0]
                model_id = model_key.split(" ")[1]
            except IndexError:
                pass
        if class_name is None:
            print("** class name missing **")
        elif class_name not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        elif model_id is None:
            print("** instance id missing **")
        else:
            model_key = class_name + "." + model_id
            delkey = None
            for key in storage.all().keys():
                if key == model_key:
                        delkey = key
                        break
            if delkey is not None:
                storage.all().pop(key)
                storage.save()
                try:
                    storage.reload()
                except FileNotFoundError:
                    pass
            else:
                print("** no instance found **")

    def do_all(self, model_type):
        """
        Prints all string representation of all instances
        based or not on the class name.

        Ex: $ all BaseModel or $ all.
        """
        obj_list = []
        if model_type == "":
            for obj in storage.all().values():
                obj_list.append(obj.__str__())
        elif model_type not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if obj.__class__.__name__ == model_type:
                    obj_list.append(obj.__str__())
        print(obj_list)

    def do_update(self, model_info):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).

        Ex: $ update BaseModel 1234-1234-1234
        email "aibnb@holbertonschool.com".
        """
        model_type = None
        model_id = None
        model_attr = None
        model_attrval = None
        if model_info != "":
            try:
                model_type = model_info.split(" ")[0]
                model_id = model_info.split(" ")[1]
                model_attr = model_info.split(" ")[2]
                model_attrval = model_info.split(" ")[3]
                if model_attrval.startswith('"'):
                    model_attrval = model_info.split(" ")[3].strip('"')
                    model_attrval += " " + model_info.split(" ")[4].strip('"')
            except IndexError:
                pass
        if model_type is None:
            print("** class name missing **")
        elif model_id is None:
            print("** instance id missing **")
        elif model_attr is None:
            print("** attribute name missing **")
        elif model_attrval is None:
            print("** value missing **")
        else:
            model_key = model_type + "." + model_id
            key_exists = False
            for key in storage.all().keys():
                if key == model_key:
                    obj = storage.all().get(key)
                    setattr(obj, model_attr, model_attrval)
                    key_exists = True
                    break
            if key_exists is not True:
                print("** no instance found **")

# only starts loop if interactive

if __name__ == "__main__":
    HBNBCommand().cmdloop()
