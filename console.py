#!/usr/bin/python3
"""The entry point to the HBnB console"""
import cmd
from models.base_model import *
from models.state import *
from models.city import *
from models.user import *
from models.review import *
from models.place import *


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

# Runs Commands

    # checks for existance of command
    def onecmd(self, line):
        """compares given command to available commands"""
        iscommand = super(HBNBCommand, self).onecmd(line)
        return (iscommand)

# All Support Commands:

    # Quit command to exit the program
    def do_quit(self, s):
        """Quit command to exit the program"""
        exit()

    # def help_quit(self):
    #     """ help info for quit and eof command """
    #     print("Quit command to exit the program\n")

    # Makes eof command point to quit code
    # makes document the same too
    do_EOF = do_quit
    # help_EOF = help_quit

    def do_create(self, model_type):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Ex: $ create BaseModel
        """
        if model_type == "":
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
            # SAVE new_model TO JSON!!!!!!!!!!!!!!!!!

    def do_show(self, class_name, model_id):
        """
        Prints the string representation of an instance
        based on the class name and id.

        Ex: $ show BaseModel 1234-1234-1234.
        """
        if class_name == "":
            print("** class name missing **")
        elif class_name not in ["BaseModel", "City", "State",
                                "User", "Review", "Place", "Amenity"]:
            print("** class doesn't exist **")
        else:
            if model_id == "":
                print("** instance id missing **")
            # else:
            #    show stuff here

# only execute if interactive
if __name__ == "__main__":
    """Beginning of the interactive portion of the console"""
    # Creates HBNBCommand class named hbnb
    hbnb = HBNBCommand()
    # Starts looping in hbnb console
    hbnb.cmdloop()
