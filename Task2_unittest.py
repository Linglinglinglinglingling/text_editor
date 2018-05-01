"""
@author: Lingling Yao
@since: 26/04/2018
@modified: 01/05/2018
@functionality: Task5: This file implements unittest f or all modules in achieving Task2 (A ArrayBased List class and two
                sorting functions).
"""


import Task2_SortingsFunction
from Task2_ArrayListClass import ArrayList
import unittest


class TestTask2ArrayListClass(unittest.TestCase):

    def setUp(self):
        # perform set up actions (if any)
        pass

    def tearDown(self):
        # Perform clean-up actions (if any)
        pass

    def test_constructor(self):
        # constructor test
        a_object = ArrayList()
        a_object.constructor(20)
        self.assertEqual(len(a_object.array), 20, "Constructor Error")
        self.assertEqual(a_object.count, 0, "Constructor Error")

    def test_reset(self):
        # reset test
        a_object = ArrayList()
        a_object.reset(40)
        # test case 1: 40
        self.assertEqual(len(a_object.array), 40, "Reset Array Error")
        self.assertEqual(a_object.count, 0, "Reset Array Error")
        # test case 2: 60
        a_object.reset(60)
        self.assertEqual(len(a_object.array), 60, "Reset Array Error")
        self.assertEqual(a_object.count, 0, "Reset Array Error")
        # test case 3: 20
        a_object.reset(20)
        self.assertEqual(len(a_object.array), 20, "Reset Array Error")
        self.assertEqual(a_object.count, 0, "Reset Array Error")
        # valid/invalid?

    def test_is_full(self):
        # is_full test
        a_object = ArrayList()
        for i in range(20):
            a_object.append(i)
        # though it is dynamic, the list could be full, since the dynamic is provided before appending, it is not
        # checked after appending. (Only insert or append on a full list could trigger the dynamic_extend method)
        self.assertEqual(a_object.is_full(), True, "is_full Array ERROR")
        self.assertEqual(len(a_object), 20, "is_full Array ERROR")
        self.assertEqual(len(a_object.array), 20, "is_full Array ERROR")
        a_object.append(33)
        self.assertEqual(a_object.is_full(), False, "is_full Array ERROR")
        self.assertEqual(len(a_object), 21, "is_full Array ERROR")
        self.assertEqual(len(a_object.array), 40, "is_full Array ERROR")

    def test_is_empty(self):
        # is_empty test
        a_object = ArrayList()
        # test case 1
        self.assertEqual(a_object.is_empty(), True, "is_empty Array ERROR")
        self.assertEqual(a_object.count, 0, "is_empty Array ERROR")
        # test case 2
        a_object.append(1)
        self.assertEqual(a_object.is_empty(), False, "is_empty Array ERROR")
        self.assertEqual(a_object.count, 1, "is_empty Array ERROR")

    def test_len(self):
        # __len__ test
        a_object = ArrayList()
        # test case 1: empty
        self.assertEqual(len(a_object), 0, "__len__ Array Error")
        # test case 2: not empty
        for i in range(5):
            a_object.append(i)
        self.assertEqual(len(a_object), 5, "__len__ Array Error")
        for i in range(5):
            a_object.append(i)
        self.assertEqual(len(a_object), 10, "__len__ Array Error")

    def test_append(self):
        # append test
        test_object = ArrayList()
        # test case 1: append 1
        test_object.append(1)
        self.assertEqual(test_object[0], 1, "Append Array Error")
        # test case 2: append 2
        test_object.append(2)
        self.assertEqual(test_object[0], 1, "Append Array Error")
        self.assertEqual(test_object[1], 2, "Append Array Error")
        # test case 3: append 3
        test_object.append(3)
        self.assertEqual(test_object[0], 1, "Append Array Error")
        self.assertEqual(test_object[1], 2, "Append Array Error")
        self.assertEqual(test_object[2], 3, "Append Array Error")

    def test_contains(self):
        # __contains__ test
        test_object = ArrayList()
        # test case 1
        for i in range(5):
            test_object.append(i)
        self.assertEqual((4 in test_object), True, "__Contains__ Error")
        self.assertEqual((0 in test_object), True, "__Contains__ Error")
        # test case 2
        for i in range(5):
            test_object.append(i + 5)
        self.assertEqual((9 in test_object), True, "__Contains__ Error")
        self.assertEqual((10 in test_object), False, "__Contains__ Error")

    def test_str(self):
        # __str__ test
        test_object = ArrayList()
        for i in range(5):
            test_object.append(i)
        # test case 1
        self.assertEqual(str(test_object), "0\n1\n2\n3\n4\n", "__Str__ Error")
        # test case 2
        for i in range(5):
            test_object.append(i + 5)
        self.assertEqual(str(test_object), "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n", "__Str__ Error")
        # test case 3
        for i in range(5):
            test_object.append(i)
        self.assertEqual(str(test_object), "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n0\n1\n2\n3\n4\n", "__Str__ Error")

    def test_getitem(self):
        # __getitem__ test
        test_object = ArrayList()
        for i in range(25):
            test_object.append(i)
        self.assertEqual(test_object[0], 0, "__getitem__ Error")
        self.assertEqual(test_object[24], 24, "__getitem__ Error")
        self.assertEqual(test_object[3], 3, "__getitem__ Error")
        self.assertEqual(test_object[-1], 24, "__getitem__ Error")
        self.assertEqual(test_object[-25], 0, "__getitem__ Error")

    def test_setitem(self):
        # __setitem__ test
        test_object = ArrayList()
        for i in range(26):
            test_object.append(i)
        for i in range(len(test_object)):
            test_object[i] = i + 1
        for i in range(len(test_object)):
            self.assertEqual(test_object[i], i + 1, "__setitem__ Error")
        self.assertEqual(test_object[-1], 26, "__setitem__ Error")
        self.assertEqual(test_object[-26], 1, "__setitem__ Error")

    def test_eq(self):
        # __eq__ test
        test_object = ArrayList()
        # test case 1
        for i in range(5):
            test_object.append(i)
        self.assertNotEqual(test_object, [0, 1, 2, 3, 4, 5], "__eq__ Error")
        self.assertEqual(test_object, [0, 1, 2, 3, 4], "__eq__ Error")
        self.assertNotEqual(test_object, [0, 1, 2, 3, 5], "__eq__ Error")
        # test case 2
        test_object = test_object.reset(27)
        other = []
        for i in range(27):
            test_object.append(i)
            other.append(i)
        self.assertEqual(test_object, other, "__eq__ Error")

    def test_insert(self):
        # insert test
        test_object = ArrayList()
        for i in range(5):
            test_object.append(i)
        test_object.insert(0, 11)
        self.assertEqual(str(test_object), "11\n0\n1\n2\n3\n4\n", "Insert Error")
        self.assertEqual(test_object[0], 11, "Insert Error")
        self.assertEqual(test_object[1], 0, "Insert Error")
        self.assertEqual(len(test_object), 6, "Insert Error")
        test_object.insert(-1, 12)
        self.assertEqual(str(test_object), "11\n0\n1\n2\n3\n12\n4\n", "Insert Error")
        self.assertEqual(test_object[-2], 12, "Insert Error")
        self.assertEqual(test_object[6], 4, "Insert Error")
        self.assertEqual(test_object[5], 12, "Insert Error")
        self.assertEqual(len(test_object), 7, "Insert Error")

    def test_delete(self):
        # delete test
        test_object = ArrayList()
        for i in range(5):
            test_object.append(i)
        # test case 1
        test_object.delete(3)
        self.assertEqual(str(test_object), "0\n1\n2\n4\n", "Delete Error")
        self.assertEqual(test_object[3], 4, "Delete Error")
        self.assertEqual(len(test_object), 4, "Delete Error")
        # test case 2
        test_object.delete(-1)
        self.assertEqual(str(test_object), "0\n1\n2\n", "Delete Error")
        self.assertEqual(test_object[2], 2, "Delete Error")
        self.assertEqual(len(test_object), 3, "Delete Error")

    def test_remove(self):
        # remove test
        test_object = ArrayList()
        for i in range(5):
            test_object.append(i)
        # test case 1
        test_object.remove(3)
        self.assertEqual(str(test_object), "0\n1\n2\n4\n", "Remove Error")
        self.assertEqual(test_object[3], 4, "Remove Error")
        self.assertEqual(len(test_object), 4, "Remove Error")
        # test case 2
        test_object.remove(0)
        self.assertEqual(str(test_object), "1\n2\n4\n", "Remove Error")
        self.assertEqual(test_object[2], 4, "Remove Error")
        self.assertEqual(len(test_object), 3, "Remove Error")

    def test_sort(self):
        # sort test
        test_object = ArrayList()
        test_object.append(33)
        test_object.append(243)
        test_object.append(2)
        test_object.append(1)
        test_object.append(7)
        # test case 1: as
        test_object.sort(0)
        self.assertEqual(str(test_object), "1\n2\n7\n33\n243\n", "As Sort Error")
        # test case 2: de
        test_object.sort(1)
        self.assertEqual(str(test_object), "243\n33\n7\n2\n1\n", "As Sort Error")

    def test_extend_dynamic(self):
        # extend_dynamic test
        test_object = ArrayList()
        for i in range(20):
            test_object.append(i)
        # Appending
        test_object.append(20)
        self.assertEqual(len(test_object), 21, "Extend_dynamic Append Error")
        self.assertEqual(len(test_object.array), 40, "Extend_dynamic Append Error")
        for i in range(19):
            test_object.append(i)
        self.assertEqual(len(test_object), 40, "Extend_dynamic Append Error")
        self.assertEqual(len(test_object.array), 40, "Extend_dynamic Append Error")
        # Inserting
        test_object.reset(20)
        for i in range(20):
            test_object.append(i)
        test_object.insert(0, 200)
        self.assertEqual(len(test_object), 21, "Extend_dynamic Append Error")
        self.assertEqual(len(test_object.array), 40, "Extend_dynamic Append Error")
        for i in range(19):
            test_object.insert(20+i, i)
        self.assertEqual(len(test_object), 40, "Extend_dynamic Append Error")
        self.assertEqual(len(test_object.array), 40, "Extend_dynamic Append Error")

    def test_shrink_dynamic(self):
        # shrink_dynamic test
        test_object = ArrayList()
        for i in range(40):
            test_object.append(i)
        # delete test case 1
        for i in range(35):
            test_object.delete(0)
        self.assertEqual(len(test_object), 5, "Shrink_dynamic Delete Error")
        self.assertEqual(len(test_object.array), 40, "Shrink_dynamic Delete Error")
        test_object.delete(0)
        self.assertEqual(len(test_object), 4, "Shrink_dynamic Delete Error")
        self.assertEqual(len(test_object.array), 20, "Shrink_dynamic Delete Error")
        # delete test case 2
        test_object.reset(160)
        for i in range(160):
            test_object.append(i)
        for i in range(140):
            test_object.delete(0)
        self.assertEqual(len(test_object), 20, "Shrink_dynamic Delete Error")
        self.assertEqual(len(test_object.array), 160, "Shrink_dynamic Delete Error")
        test_object.delete(0)
        self.assertEqual(len(test_object), 19, "Shrink_dynamic Delete Error")
        self.assertEqual(len(test_object.array), 80, "Shrink_dynamic Delete Error")
        # remove test case 1
        test_object.reset(40)
        for i in range(40):
            test_object.append(i)
        for i in range(35):
            test_object.remove(i)
        self.assertEqual(len(test_object), 5, "Shrink_dynamic Delete Error")
        self.assertEqual(len(test_object.array), 40, "Shrink_dynamic Delete Error")
        test_object.remove(35)
        self.assertEqual(len(test_object), 4, "Shrink_dynamic Delete Error")
        self.assertEqual(len(test_object.array), 20, "Shrink_dynamic Delete Error")
        # remove test case 2
        test_object.reset(160)
        for i in range(160):
            test_object.append(i)
        for i in range(140):
            test_object.remove(i)
        self.assertEqual(len(test_object), 20, "Shrink_dynamic Delete Error")
        self.assertEqual(len(test_object.array), 160, "Shrink_dynamic Delete Error")
        test_object.remove(140)
        self.assertEqual(len(test_object), 19, "Shrink_dynamic Delete Error")
        self.assertEqual(len(test_object.array), 80, "Shrink_dynamic Delete Error")


class Task2SortingFunctionInsertionAs(unittest.TestCase):

    def setUp(self):
        # perform set up actions (if any)
        pass

    def tearDown(self):
        # Perform clean-up actions (if any)
        pass

    def test_insertion_sort_as_int(self):
        # insertion_sort_as integer test
        test_list = [4, 2, 6, 243, 1, 2]
        Task2_SortingsFunction.insertion_sort_as(test_list)
        self.assertEqual(test_list, [1, 2, 2, 4, 6, 243], "Insertion Sort As int ERROR")
        test_list = [13521, 434, 2, 1, 5]
        Task2_SortingsFunction.insertion_sort_as(test_list)
        self.assertEqual(test_list, [1, 2, 5, 434, 13521], "Insertion Sort As int ERROR")

    def test_insertion_sort_as_string(self):
        # insertion_sort_as string test
        test_list = ['f', 'e', 'd', 'c', 'b', 'a']
        Task2_SortingsFunction.insertion_sort_as(test_list)
        self.assertEqual(test_list, ['a', 'b', 'c', 'd', 'e', 'f'], "Insertion Sort As str ERROR")
        test_list = ['finger', 'eat', 'dance', 'cab', 'body', 'apple']
        Task2_SortingsFunction.insertion_sort_as(test_list)
        self.assertEqual(test_list, ['apple', 'body', 'cab', 'dance', 'eat', 'finger'], "Insertion Sort As str ERROR")


class Task2SortingFunctionInsertionDe(unittest.TestCase):
    def setUp(self):
        # perform set up actions (if any)
        pass

    def tearDown(self):
        # Perform clean-up actions (if any)
        pass

    def test_insertion_sort_de_int(self):
        # insertion_sort_de integer test
        test_list = [1, 2, 3, 4, 5]
        Task2_SortingsFunction.insertion_sort_de(test_list)
        self.assertEqual(test_list, [5, 4, 3, 2, 1], "Insertion Sort De int ERROR")
        test_list = [4352, 2315, 342, 13, 5, 111]
        Task2_SortingsFunction.insertion_sort_de(test_list)
        self.assertEqual(test_list, [4352, 2315, 342, 111, 13, 5], "Insertion Sort De int ERROR")

    def test_insertion_sort_de_str(self):
        # insertion_sort_de string test
        test_list = ['a', 'b', 'c', 'd', 'e', 'f']
        Task2_SortingsFunction.insertion_sort_de(test_list)
        self.assertEqual(test_list, ['f', 'e', 'd', 'c', 'b', 'a'], "Insertion Sort De int ERROR")
        test_list = ['apple', 'body', 'cab', 'dance', 'eat', 'finger']
        Task2_SortingsFunction.insertion_sort_de(test_list)
        self.assertEqual(test_list, ['finger', 'eat', 'dance', 'cab', 'body', 'apple'], "Insertion Sort De int ERROR")


if __name__ == "__main__":
    unittest.main()

    print("REACHED")
