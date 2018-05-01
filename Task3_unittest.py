"""
@author: Lingling Yao
@since: 26/04/2018
@modified: 01/05/2018
@functionality: Task3: This file implements unittest for all modules in achieving Task3 (A LinkedList class and an
                iterator class).
                The two sorting functions used in this task is already tested in Task2, it wouldn't be tested here
                again.
"""


from Task3_LinkedListClass import LinkedList
from Task3_iteratorClass import LinkedIterator


def test_len(test_object):
    # test case 1: empty
    assert len(test_object) == 0, "__len__ Error"
    # test case 2: not empty
    '''for i in range(5):
        test_object.append(i)
    assert len(test_object) == 5, "__len__ Error"
    for i in range(5):
        test_object.append(i)
    assert len(test_object) == 10, "__len__ Error"'''

def test_append(test_object):
    # test case 1: append 1
    test_object.append(1)
    assert len(test_object) == 1, "Append Error"
    # test case 2: append 2
    test_object.append(2)
    assert test_object[0] == 1, "Append Error"
    assert test_object[1] == 2, "Append Error"
    # test case 3: append 3
    test_object.append(3)
    assert test_object[0] == 1, "Append Error"
    assert test_object[1] == 2, "Append Error"
    assert test_object[2] == 3, "Append Error"
    assert len(test_object) == 3, "Append Error"


def test_contains(test_object):
    for i in range(5):
        test_object.append(i)
    assert (4 in test_object) == True, "__Contains__ Error"
    assert (0 in test_object) == True, "__Contains__ Error"
    for i in range(5):
        test_object.append(i + 5)
    assert (9 in test_object) == True, "__Contains__ Error"
    # assert (10 in test_object) == True, "__Contains__ Error"
    assert (10 in test_object) == False, "__Contains__ Error"


def test_str(test_object):
    for i in range(5):
        test_object.append(i)
    assert str(test_object) == "0\n1\n2\n3\n4\n", "__str__ Error"
    for i in range(5):
        test_object.append(i + 5)
    assert str(test_object) == "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n", "__str__ Error"
    for i in range(5):
        test_object.append(i)
    assert str(test_object) == "0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n0\n1\n2\n3\n4\n", "__str__ Error"


def test_getitem(test_object):
    for i in range(25):
        test_object.append(i)
    assert test_object[0] == 0, "__getitem__ Error"
    assert test_object[24] == 24, "__getitem__ Error"
    assert test_object[3] == 3, "__getitem__ Error"
    assert test_object[-1] == 24, "__getitem__ Error"
    assert test_object[-25] == 0, "__getitem__ Error"


def test_setitem(test_object):
    for i in range(26):
        test_object.append(i)
    for i in range(len(test_object)):
        test_object[i] = i + 1
    for i in range(len(test_object)):
        assert test_object[i] == i + 1, "__setitem__ Error"
    assert test_object[-1] == 26, "__setitem__ Error"
    assert test_object[-26] == 1, "__setitem__ Error"


def test_eq(test_object):
    for i in range(5):
        test_object.append(i)
    assert not test_object == [0, 1, 2, 3, 4, 5], "__eq__ Error"
    assert test_object == [0, 1, 2, 3, 4], "__eq__ Error"
    assert not test_object == [0, 1, 2, 3, 5], "__eq__ Error"
    # another test case
    test_object.reset()
    other = []
    for i in range(27):
        test_object.append(i)
        other.append(i)
    assert test_object == other, "__eq__ Error"


def test_insert(test_object):
    for i in range(5):
        test_object.append(i)
    test_object.insert(0, 11)
    assert str(test_object) == "11\n0\n1\n2\n3\n4\n", "Insert Error"
    assert test_object[0] == 11, "Insert Error"
    test_object.insert(-1, 12)
    assert str(test_object) == "11\n0\n1\n2\n3\n12\n4\n"
    assert test_object[-2] == 12, "Insert Error"


def test_delete(test_object):
    for i in range(5):
        test_object.append(i)
    # test case 1
    test_object.delete(3)
    assert str(test_object) == "0\n1\n2\n4\n", "Delete Error"
    assert test_object[3] == 4, "Delete Error"
    assert len(test_object) == 4, "Delete Error"
    # test case 2
    test_object.delete(-1)
    assert str(test_object) == "0\n1\n2\n", "Delete Error"
    assert test_object[2] == 2, "Delete Error"
    assert len(test_object) == 3, "Delete Error"


def test_remove(test_object):
    for i in range(5):
        test_object.append(i)
    # test case 1
    test_object.remove(3)
    assert str(test_object) == "0\n1\n2\n4\n", "Remove Error"
    assert test_object[3] == 4, "Remove Error"
    assert len(test_object) == 4, "Remove Error"
    # test case 2
    test_object.remove(0)
    assert str(test_object) == "1\n2\n4\n", "Remove Error"
    assert test_object[2] == 4, "Remove Error"
    assert len(test_object) == 3, "Remove Error"
    # test_object.remove(5)


def test_sort(test_object):
    test_object.append(33)
    test_object.append(243)
    test_object.append(2)
    test_object.append(1)
    test_object.append(7)
    # test case 1: as
    test_object.sort(0)
    assert str(test_object) == "1\n2\n7\n33\n243\n", "As Sort Error"
    # test case 2: de
    test_object.sort(1)
    assert str(test_object) == "243\n33\n7\n2\n1\n", "De Sort Error"


def test_iterator(test_object):
    for i in range(5):
        test_object.append(i + 22)
    for i in test_object:
        print(i)
        # can't call __str__, is i an instance of the object?
        # Is it that only an object can call the methods, an instance cannot?
    test_iterator = LinkedIterator(test_object.head)
    for i in test_iterator:
        print(i)


if __name__ == "__main__":
    # __len__ test
    a_object = LinkedList()
    test_len(a_object)
    # append test
    b_object = LinkedList()
    test_append(b_object)
    # insert test
    b_object.reset()
    test_insert(b_object)
    # __getitem__ test
    b_object.reset()
    test_getitem(b_object)
    # __contains__ test
    b_object.reset()
    test_contains(b_object)
    # __setitem__ test
    b_object.reset()
    test_setitem(b_object)
    # __eq__ test
    b_object.reset()
    test_eq(b_object)
    # delete test
    b_object.reset()
    test_delete(b_object)
    # remove test
    b_object.reset()
    test_remove(b_object)
    # sort test
    b_object.reset()
    test_sort(b_object)
    # iterator test
    b_object.reset()
    test_iterator(b_object)

    print("\nREACHED")