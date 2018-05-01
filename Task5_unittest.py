"""
@author: Lingling Yao
@since: 29/04/2018
@modified: 01/05/2018
@functionality: Task5: This file implement unittest for all modules in achieving Task5 (the implementation of the
                required text editor).
"""


import Task5_editorClass
import Task5_main
import unittest


class TestTask5EditorClass(unittest.TestCase):
    def setUp(self):
        # perform set up actions (if any)
        pass

    def tearDown(self):
        # Perform clean-up actions (if any)
        pass

    def test_constructor(self):
        test_object = Task5_editorClass.Editor()
        # test unfinished

    def test_reset(self):
        test_object = Task5_editorClass.Editor()
        # test unfinished

    def test_deep_reset(self):
        test_object = Task5_editorClass.Editor()
        # test unfinished

    def test_insert(self):
        pass

    def test_print(self):
        pass

    def test_delete(self):
        pass

    def test_search(self):
        pass

    def test_read(self):
        pass

    def test_write(self):
        pass

    def test_receive_user_command(self):
        # test with receive_user_command's output
        test_object = Task5_editorClass.Editor()
        # test case 1
        self.assertEqual(test_object.receive_user_command("READ"), True, "receive_user_command ERROR")
        self.assertEqual(test_object.receive_user_command("INSERT"), True, "receive_user_command ERROR")
        self.assertEqual(test_object.receive_user_command("WRITE"), True, "receive_user_command ERROR")
        self.assertEqual(test_object.receive_user_command("PRINT"), True, "receive_user_command ERROR")
        self.assertEqual(test_object.receive_user_command("DELETE"), True, "receive_user_command ERROR")
        self.assertEqual(test_object.receive_user_command("SEARCH"), True, "receive_user_command ERROR")
        self.assertEqual(test_object.receive_user_command("QUIT"), True, "receive_user_command ERROR")
        self.assertEqual(test_object.receive_user_command("HELP"), True, "receive_user_command ERROR")

    def test_tellme_user_command(self):
        test_object = Task5_editorClass.Editor()
        test_object.user_command = "READ"
        self.assertEqual(test_object.tellme_user_command(), "READ", "is_quit ERROR")
        test_object.user_command = "WRITE"
        self.assertEqual(test_object.tellme_user_command(), "WRITE", "is_quit ERROR")

    def test_is_quit(self):
        # test with is_quit()
        test_object = Task5_editorClass.Editor()
        # test case 1: not quit
        test_object.user_command = "READ"
        self.assertEqual(test_object.is_quit(), False, "is_quit ERROR")
        # test case 2: quit
        test_object.user_command = "QUIT"
        self.assertEqual(test_object.is_quit(), True, "is_quit ERROR")


class TestTask5CommandAdditionCheck(unittest.TestCase):

    def test_HELP(self):
        # valid input
        self.assertEqual(Task5_main.command_addition_check("HELP", []), True, "command_addition_check ERROR")
        # invalid input
        self.assertEqual(Task5_main.command_addition_check("HELP", ["1"]), False, "command_addition_check ERROR")

    def test_quit(self):
        # valid input
        self.assertEqual(Task5_main.command_addition_check("QUIT", []), True, "command_addition_check ERROR")
        # invalid input
        self.assertEqual(Task5_main.command_addition_check("QUIT", ["1"]), False, "command_addition_check ERROR")

    def test_insert(self):
        # valid input
        self.assertEqual(Task5_main.command_addition_check("INSERT", ["1"]), True,
                         "command_addition_check ERROR")
        # invalid input
        self.assertEqual(Task5_main.command_addition_check("INSERT", ["1", "2"]), False,
                         "command_addition_check ERROR")

    def test_read(self):
        # valid input
        self.assertEqual(Task5_main.command_addition_check("READ", ["test.txt"]), True,
                         "command_addition_check ERROR")
        # invalid input
        self.assertEqual(Task5_main.command_addition_check("READ", []), False, "command_addition_check ERROR")
        self.assertEqual(Task5_main.command_addition_check("READ", ["test.txt", "1.txt"]), False,
                         "command_addition_check ERROR")

    def test_write(self):
        # valid input
        self.assertEqual(Task5_main.command_addition_check("WRITE", ["test.txt"]), True,
                         "command_addition_check ERROR")
        # invalid input
        self.assertEqual(Task5_main.command_addition_check("WRITE", []), False, "command_addition_check ERROR")
        self.assertEqual(Task5_main.command_addition_check("WRITE", ["test.txt", "1.txt"]), False,
                         "command_addition_check ERROR")

    def test_print(self):
        # valid input
        self.assertEqual(Task5_main.command_addition_check("PRINT", []), True, "command_addition_check ERROR")
        self.assertEqual(Task5_main.command_addition_check("PRINT", ["1"]), True, "command_addition_check ERROR")
        self.assertEqual(Task5_main.command_addition_check("PRINT", ["1", "3"]), True,
                         "command_addition_check ERROR")
        # invalid input
        self.assertEqual(Task5_main.command_addition_check("PRINT", ["3", "1", "5"]), False,
                         "command_addition_check ERROR")
        self.assertEqual(Task5_main.command_addition_check("PRINT", ["1", "2", "3"]), False,
                         "command_addition_check ERROR")

    def test_delete(self):
        # valid input
        self.assertEqual(Task5_main.command_addition_check("DELETE", []), True, "command_addition_check ERROR")
        self.assertEqual(Task5_main.command_addition_check("DELETE", ["1"]), True,
                         "command_addition_check ERROR")
        # invalid input
        self.assertEqual(Task5_main.command_addition_check("DELETE", ["1", "2"]), False,
                         "command_addition_check ERROR")

    def test_search(self):
        # valid input
        self.assertEqual(Task5_main.command_addition_check("SEARCH", ["1"]), True,
                         "command_addition_check ERROR")
        # invalid input
        self.assertEqual(Task5_main.command_addition_check("SEARCH", []), False, "command_addition_check ERROR")
        self.assertEqual(Task5_main.command_addition_check("SEARCH", ["here", "fine"]), False,
                         "command_addition_check ERROR")


if __name__ == "__main__":
    unittest.main()

    print("\nREACHED")
