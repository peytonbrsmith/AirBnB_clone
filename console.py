#!/usr/bin/python3
"""The entry point to the HBnB console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    The HBNB Command Class
    ======================

    The class used to create and use all HBnB associated
    commands. Inherits from cmd.

    """
    def __init__(self):
        """initializes the HBNB command class"""
    # inits parent class attributes
        super(HBNBCommand, self).__init__()
    # sets CMD and HBNBCommand attributes
        self.prompt = "(hbnb) "

    # overrides default empty line behavior of repeating
    # last working command
    def emptyline(self):
        """repeats line on empty line"""
        pass

    # enables exitability
    def can_exit(self):
        """enables exiting of the cmd loop"""
        return True

    # checks for existance of command
    def onecmd(self, line):
        """compares given command to available commands"""
        iscommand = super(HBNBCommand, self).onecmd(line)
        return (iscommand)

    # Quit command to exit the program
    def do_quit(self, s):
        """ Quits the console upon command """
        exit()

    def help_quit(self):
        """ help info for quit and eof command """
        print("Quit command to exit the program\n")

    # Makes eof command point to quit code
    # makes document the same too
    do_EOF = do_quit
    help_EOF = help_quit

# only execute if interactive
if __name__ == "__main__":
    """Beginning of the interactive portion of the console"""
    # Creates HBNBCommand class named hbnb
    hbnb = HBNBCommand()
    # Starts looping in hbnb console
    hbnb.cmdloop()
