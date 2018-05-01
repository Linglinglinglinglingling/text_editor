"""
@author: Lingling Yao
@since: 01/05/2018
@modified: 01/05/2018
@functionality: Task5: This file contains the main() for the text editor.
"""


import Task5_editorClass


def command_addition_check(command, addition):
    """
    This function takes in the users' full command, e.g.(print 1 3), and check if it is with the appropriate additional
    command (e.g. if line number/filename is given). If the additional commands are line numbers, they would be
    converted to integers and stored back into the same list.
        For details:
            1. INSERT: one and only one line number must be given
            (addition can't be empty and it must contain only one element: an integer in string)
            2. PRINT: addition could be empty/contain one element/contain two element
            ( element must be integers in string)
            3. DELETE: addition could be empty, if it is not, only one line number should be given
            (addition contain only one element: an integer in string, or be empty)
            4. READ: one and only one filename in string format must be given
            (addition can't be empty and it must contain only one element in string)
            5. WRITE: one and only one filename in string format must be given
            (addition can't be empty and it must contain only one element in string)
            6. SEARCH: one and only one word in string format must be given
            (addition can't be empty and it must contain only one element in string)
            7. HELP: the addition must be empty
            8. QUIT: the addition must be empty
    :param command: A string: The main command (e.g. print) in upper case.
    :param addition: A python standard list: The additional command (e.g. line number(s)/filename in string)
    :return: Boolean: True if 1. with a correct amount of additional command
                              2. with the correct data type of the additional command
                      False if violate the 1-2 points above.
    :pre_condition: a command in string must be passed to the function and it must be upper cased before reach here and
                   a python standard list named addition must be passed to the fuction after the command.
    :post_condition: True or False would be returned based on the rule maintioned above.
    :time_complexity: TBC.
    """
    # tested in Task5_unittest
    # for those the addition are integers or empty
    if command in ["INSERT", "PRINT", "QUIT", "HELP", "DELETE"]:
        if command in ["QUIT", "HELP"]:
            # these command cannot have addition range
            if len(addition) > 0:
                print("?")  # error responding
                return False
        if command in ["QUIT", "HELP", "PRINT", "DELETE"]:
            # these command may or must have no addition e.g. PRINT (print the whole txt)
            if len(addition) == 0:
                return True
        if command == "INSERT":
            # insert must have one and only one given line number
            if len(addition) == 0:
                raise ValueError
        # if command have addition len 1, check 1. if the additional is overwhelmed
        if command in ["INSERT", "DELETE"]:
            if len(addition) > 1:
                print("?")  # error responding
                return False
        # 2. check the range is valid
        try:
            for i in range(len(addition)):
                addition[i] = int(addition[i])
            # PRINT is a different case
            if command == "PRINT":
                # print is able to have only one given line number
                # PRINT is the only command can have two additional commands, and if it is overwhelmed is checked here
                if len(addition) == 1:
                    return True
                if len(addition) > 2:
                    a = int('sss')
            return True
        except:
            print("?")  # error responding
            return False
    # if the addition range is a string
    else:
        if (len(addition) == 0) or (len(addition) > 1):
            print("?")  # error responding
            return False
        return True


def main():
    """
    This is the main() for the program. It would keep running until the user choose to quit or trigger exceptions in
    class in running.
    :return: None
    """
    # for each running, an object is created
    editor_object = Task5_editorClass.Editor()
    command_addition = []
    user_command = ""
    # running unless user choose to quit
    while not editor_object.is_quit():
        string_flag = 0
        # able to continue until "string_flag = 1" is reached
        while string_flag == 0:
            # user_input = ""
            user_command = ""  # hold the command, e.g. "PRINT"
            command_addition = []  # hold the addition command, e.g. ["1", "3"]
            try:
                # print prompt and receive command
                # user_input holds the complete command, e.g. "print 1 3" - > ["print", "1", "3"]
                user_input = input("Text_Editor(To see what you can do, enter 'help')>> ")
                user_input = user_input.split(" ")
                user_command = user_input.pop(0)
                user_command = user_command.upper()  # command is not case sensitive
                for i in range(len(user_input)):
                    command_addition.append(user_input[i])
                # check command addition
                if command_addition_check(user_command, command_addition) == False:
                    continue
                # let object receive command
                if editor_object.receive_user_command(user_command) is False:
                    a = int("sss")
                string_flag = 1  # the command is valid if we reach here, but not the addition command
            # Every exception happens outside the class is handled here, it is designed that any error handled here
            # would not lead to the abortion of the program.(except INSERT, if it does not
            # have a line number, the program would raise an exception and the program aborts
            # (as stated in the requirement).)
            except:
                if user_command == "INSERT" and len(command_addition) == 0:
                    raise ValueError("There should be a line number given for insertion")
                print("?")  # error responding

        # execute user command
        if editor_object.tellme_user_command() == "HELP":
            editor_object.menu()
        if editor_object.tellme_user_command() == "INSERT":
            try:
                insert_text = str(input("Enter the text (only one line): \n"))
            except TypeError:
                print("?")
                raise TypeError("Invalid text")
            line_number = command_addition[0]
            editor_object.insert(line_number, insert_text)

        elif editor_object.tellme_user_command() == "READ":
            filename = str(command_addition[0]) + ".txt"
            editor_object.read(filename)

        elif editor_object.tellme_user_command() == "WRITE":
            filename = str(command_addition[0]) + ".txt"
            editor_object.write(filename)

        elif editor_object.tellme_user_command() == "PRINT":
            if len(command_addition) == 0:
                editor_object.print()
            elif len(command_addition) == 1:
                editor_object.print(command_addition[0])
            else:
                editor_object.print(command_addition[0], command_addition[1])

        elif editor_object.tellme_user_command() == "DELETE":
            if len(command_addition) == 0:
                editor_object.delete()
            else:
                editor_object.delete(command_addition[0])

        elif editor_object.tellme_user_command() == "SEARCH":
            editor_object.research(command_addition[0])


if __name__ == "__main__":
    # program starts from here.
    main()
