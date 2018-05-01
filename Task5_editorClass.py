"""
@author: Lingling Yao
@since: 29/04/2018
@modified: 01/05/2018
@functionality: Task5: This file contains the editor class.
                notice: Every exception triggered in the class would lead to the abortion of the program.
"""


import Task2_ArrayListClass


class Editor:

    def __init__(self):
        self.valid_command = ["HELP", "INSERT", "READ", "WRITE", "PRINT", "DELETE", "SEARCH", "QUIT"]
        self.user_command = ""
        self.command_addition = []
        self.user_caching = Task2_ArrayListClass.ArrayList()

    def constructor(self):
        # self.valid_command = ["HELP", "INSERT", "READ", "WRITE", "PRINT", "DELETE", "SEARCH", "QUIT"]
        self.user_command = ""
        self.command_addition = []

    def reset(self):
        self.constructor()

    def deep_reset(self):
        self.__init__()

    def receive_user_command(self, command):
        # tested
        try:
            if command not in self.valid_command:
                t = int('sss')
            self.user_command = command
            return True  # user command received successfully
        except:
            print("?")  # error responding
            return False    # fail to receive user command

    def tellme_user_command(self):
        # tested
        return self.user_command

    def is_quit(self):
        # tested
        return self.user_command == "QUIT"

    def menu(self):
        # no need to test
        print("============================================================")
        print("->Insert lineNumber: Insert a line of text into file.")
        print("------------------------------------------------------------")
        print("->Read filename: Read the file(filename.txt)into caching.")
        print("------------------------------------------------------------")
        print("->Write filename: Open the filename(filename.txt), and \n"
              "  save the lines currently in caching in it. If the file \n"
              "  does not exist, it would be created.")
        print("------------------------------------------------------------")
        print("->Print lineNum1 lineNum2: Display the content in caching \n"
              "  to the screen. (A range of lines could be specified.")
        print("------------------------------------------------------------")
        print("->Delete lineNum: Delete the line at the given line number. \n"
              " (If no line number provide, all lines would be deleted.")
        print("------------------------------------------------------------")
        print("->Search word: Found the line number where the given word \n"
              "  first appears.")
        print("------------------------------------------------------------")
        print("->Quit: quit the editor.")
        print("============================================================")

    def insert(self, line_num, text=""):
        # - line number could be given
        if len(self.user_caching) == 0:
            print("?")
            raise IndexError("Index out of range: No where to insert: caching Empty")
        # line number 0 is considered invalid
        elif not (-len(self.user_caching) <= line_num <= len(self.user_caching) and line_num != 0):
            print("?")
            raise IndexError("Index out of range: Line unreachable")
        else:
            if line_num > 0:
                self.user_caching.insert(line_num - 1, text)
            else:
                self.user_caching.insert(line_num, text)

    def print(self, line_num1=None, line_num2=None):
        # - line number could be given
        if len(self.user_caching) == 0:
            print("?")
            raise IndexError("Index out of range: Content not found: caching Empty")
        if line_num1 is not None:
            if not ((-len(self.user_caching) <= line_num1 <= len(self.user_caching)) and line_num1 != 0):
                print(-len(self.user_caching))
                raise IndexError("Index out of range")
            if line_num1 < 0:
                line_num1 = (-line_num1) + (len(self.user_caching) - (-line_num1)*2) + 1
        if line_num2 is not None:
            if not ((-len(self.user_caching) <= line_num2 <= len(self.user_caching)) and line_num2 != 0):
                raise IndexError("Index out of range")
            if line_num2 < 0:
                line_num2 = (-line_num2) + (len(self.user_caching) - (-line_num2) * 2) + 1
        # to print, line number is added and saved to a temp ArrayList with the content
        tmp_caching = Task2_ArrayListClass.ArrayList()
        line_num = 0
        for line in self.user_caching:
            tmp_caching.append(str(line_num + 1) + " >> " + line)
            line_num += 1
        # start printing
        if (line_num1 is None) and (line_num2 is None):
            print("")
            str(tmp_caching)
        elif (not (line_num1 is None)) and (line_num2 is None):
            print("")
            for index in range(line_num1 - 1, len(tmp_caching)):
                print(str(tmp_caching[index]))
            print("")
        else:
            if line_num2 <= line_num1:
                raise IndexError("Index out of range: line numbers unreachable")
            print("")
            for index in range(line_num1 - 1, line_num2):
                print(str(tmp_caching[index]))
            print("")

    def read(self, filename):
        # whenever user choose to read a file, the editor would clean up the caching and make sure the caching only
        # contain the file content the user is currently interacting with (only one file at a time)
        self.deep_reset()
        try:
            the_file = open(filename, "r")
        except FileNotFoundError:
            raise FileNotFoundError("No such file found")
        for line in the_file:
            line = line.strip("\n")
            self.user_caching.append(line)
        the_file.close()

    def write(self, filename):
        # this method could use to create an empty txt file
        the_file = open(filename, "w")
        for line in self.user_caching:
            line = line + "\n"
            the_file.write(line)
        the_file.close()

    def delete(self, line_num=None):
        if len(self.user_caching) == 0:
            raise IndexError("Index out of range: Nothing to delete: caching empty")
        if line_num is None:
            self.deep_reset()
        else:
            if line_num < 0:
                line_num = (-line_num) + (len(self.user_caching) - (-line_num) * 2) + 1
            self.user_caching.delete(line_num - 1)

    def research(self, word):
        tmp_caching = Task2_ArrayListClass.ArrayList()
        for line in self.user_caching:
            tmp_caching.append(line.upper())
        word_used = word.upper()
        research_result = []
        for i in range(len(tmp_caching)):
            if word_used in tmp_caching[i]:
                research_result.append(i + 1)
        if len(research_result) == 0:
            print("Word: '" + word + "' not found")
        else:
            result_display = str("'" + word + "' is found in line(s): ")
            for i in research_result:
                result_display += str(i) + " "
            print(result_display)
        print("")
