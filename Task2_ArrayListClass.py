"""
@author: Lingling Yao
@since: 26/04/2018
@modified: 01/05/2018
@functionality: Task2: This file contains a Array-based List class with dynamic size.
"""


from referential_array import build_array
from Task2_SortingsFunction import insertion_sort_as
from Task2_SortingsFunction import insertion_sort_de
from Task1_ArrayListIterator import ArrayListIterator


class ArrayList:

    def __init__(self):
        """
        This is a constructor for class ArrayList with dynamic size.
        :param: None.
        :return: None.
        :exception: NONE.
        :pre-condition: create an object for this class.
        :post-condition: An array-based list object with a size 20 will be created.
        :complexity: O(1)
        """
        self.array = build_array(1)
        self.count = 0
        self.base_size = 20
        self.constructor(self.base_size)

    def constructor(self, base_size):
        """
        This is a method create an array with given.
        :param: base_size.
        :return: None.
        :exception: The base_size must be a positive integer.
        :pre-condition: A base_size must be given and must be a positive integer
        :post-condition: An array-based list object with a base_size size will be created, and the self.count would
                         be set to 0.
        :Time-complexity: O(N) where N is the base size.
        """
        self.array = build_array(base_size)
        self.count = 0

    def reset(self, new_base_size):
        """
        This method reset the array.
        :param new_base_size: a size of the self.array.
        :return: self: the object.
        :exception: The new_base_size must be a positive integer.
        :pre-condition: A new_base_size must be given and it must be a positive integer.
        :post_condition: The ArrayList object would be reset with a new_base_size size, and the object itself would be
                         returned.
        :Time-complexity: O(N) where N is the the value of new_base_size.
        """
        self.base_size = new_base_size
        self.constructor(self.base_size)
        self.count = 0
        return self

    def __len__(self):
        """
        This method returns the size of the List, which is the self.count of the object.
        :param: None.
        :return: self.count, the length of the ArrayBased List.
        :exception: None.
        :pre-condition: None.
        :post-condition: The size of the list, which is the self.count of the object would be returned.
        :Time-complexity: O(1)
        """
        return self.count

    def is_full(self):
        """
        This method tell the user is their ArrayBased list is full.
        :param: None.
        :return: Boolean: True is the list is full, false otherwise.
        :exception: None.
        :pre-condition: None.
        :post-condition: A boolean would be returned: True if the ArrayBased List is full, false otherwise.
        :Time-complexity: O(1)
        """
        return self.count == len(self.array)

    def is_empty(self):
        """
        This method tells the user is the ArrayBased List is empty.
        :param: None.
        :return: Boolean: True if the ArrayBased List is empty, false otherwise.
        :exception: None.
        :pre-condition: None.
        :post-condition: A boolean would be returned: True if the ArrayBased List is full, false otherwise.
        :Time-complexity: O(1)
        """
        return self.count == 0

    def __contains__(self, item):
        """
        This method checks if an item is in the ArrayBased List.
        :param item: The item user want to check if is in the list.
        :return: Boolean: True if the item found in the list, false otherwise.
        :exception: The ArrayBased could not be empty, or am AssertionError would be raised.
        :pre-condition: An item must be given by the user.
        :post-condition: A boolean would be returned: True is the item is in the list, false otherwise.
        :Time-complexity: O(N) where N is the position of the given element in the list. N is the length of the list if
                          the item is not found.
        """
        assert self.is_empty() is False, "The list is empty"
        for i in range(len(self)):
            if self.array[i] == item:
                return True
        return False

    def __str__(self):
        """
        This method convert every element in the ArrayBase List, and print them as one string with each element in each
        line. The string would also be returned.
        :param: None.
        :return: string: The string with elements in the list.
        :exception: The ArrayBased could not be empty, or an AssertionError would be raised.
        :pre-condition: The list could not be empty.
        :post-condition: A string with all the element in the list separated by \n would be returned.
        :Time-complexity: O(N) where N is the length of the list.
        """
        assert self.is_empty() is False, "The list is empty"
        string = ""
        for i in range(len(self)):
                string += str(self.array[i]) + "\n"
        print(string)
        return string

    def __getitem__(self, index):
        """
        This methods gives the user the item at the given index. Nagetive index is acceptable: self[-1] = self[len - 1],
        ...... self[-len] = self[0].
        :param index: An integer index given by the user.
        :return: The item at the given index in the list.
        :exception: The index given must be within the range: from -len to len, or IndexError would be raised.
        :pre-condition: An integer index within valid range must be given.
        :post-condition: An item at the given index would be returned.
        :Time-complexity: O(N) where N is the value of index.
        """
        if not (-len(self) >= index < len(self)):
            raise IndexError("list index out of range")
        # positive index
        if index >= 0:
            return self.array[index]
        # negative index
        else:
            index = (-index) + (self.count - (-index)*2)
            return self.array[index]

    def __setitem__(self, index, item):
        """
        This method received an index and set the element at the given index to the given item.
        :param index: An index (integer number) given by the user.
        :param item: An item given by the user.
        :return: None
        :exception: The given index must be within the range (-len)~(len) - 1, or IndexError would be raised..
        :pre-condition: An index and an item must be given and the index must be within the range.
        :post-condition: The given item would be wrote to the given position(index).
        :Time-complexity: O(N) where N is the value of index.
        """
        # do i need to check if index is a integer?
        if not (-len(self) <= index < len(self)):
            raise IndexError("list index out of range")
        if index >= 0:
            self.array[index] = item
        else:
            index = (-index) + (self.count - (-index)*2)
            self.array[index] = item

    def __eq__(self, other):
        """
        This method checks if the ArrayBased List is the same as the given list 'other'.
        :param other: An list that the user want to check if is the same as the ArrayBased List.
        :return: Boolean: True if the lists are the same, false otherwise.
        :exception: 'other' must be a list.
        :pre-condition: The 'other' must be a list.
        :post-condition: A boolean would be return: True if the lists are the same, false otherwise.
        :Time-complexity: O(1) if the lists have different size. O(N) where N is the length of the lists.
        """
        # do i need to check if other is a list? how?
        if len(self) == len(other):
            for i in range(len(self)):
                if self[i] == other[i]:
                    continue
                else:
                    return False
            return True
        else:
            return False

    def append(self, item):
        """
        This method append the given item to the end of the list.
        Before append, if the list is full, the size would double itself automatically.
        If the list is full afterwards, it size would not be changed.
        :param item: An item given by the user.
        :return: None.
        :exception: None.
        :pre-condition: An item must be given.
        :post-condition: The given item would be added to the end of the list.
        :Time-complexity: 1. O(N) where N is the size of the list.
        """
        self.extend_dynamic()
        assert not self.is_full(), "The list is full"
        self.array[self.count] = item
        self.count += 1

    def insert(self, index, item):
        """
        This method inserts an item to an given index.
        If the list is full before insertion, the list size would be doubled automatically.
        If the list is full after insertion, nothing would be changed.
        :param index: An integer index given by the user.
        :param item: An item given by the user.
        :return: None.
        :pre-condition: The index must be within the range -len~len-1, or an IndexError would be raised.
        :post-condition: The given item would be inserted at the given index.
        :Time-complexity: O(N) where N is the value of index if the list is not full before insertion.
                          O(N) where N is the len of the list if the list if full before insertion.
        """
        # do i need to check if index is an integer?
        self.extend_dynamic()
        assert not self.is_full(), "The list is full"
        if not (-len(self) <= index < len(self)):
            raise IndexError("list index out of range")
        # positive index
        if index >= 0:
            start = index
        # otherwise
        else:
            index = (-index) + (self.count - (-index)*2)
            start = index
        # moving items backwards
        self.count += 1
        for i in range(self.count - 1, start - 1, -1):
            # print("length:", len(self))
            # print("i+1:", (i+1), "i:", i)
            self[i] = self[i - 1]
        self[index] = item

    def remove(self, item):
        """
        This method removes the first appearance of the given item from the list. An error would be raised if the item
        is not
        found.
        :param item: An item given by user.
        :return: None.
        :exception: An ValueError would be raised if the item is not in the list.
        :pre-condition: Item must be in the list.
        :post-condition: The first appearance of the given item would be removed from the list.
        :Time-complexity: O(N) where N is the index of the first appearance of the item.
                          O(N) where N is the length of the list if the item not found.
        """
        for i in range(len(self)):
            if self[i] == item:
                self.delete(i)
                return
        raise ValueError("Item not found")

    def delete(self, index):
        """
        This method delete the element at the given index, and move everything after the index forward.
        After deleting, the size of the list would be half (but always bigger than 20) if the size smaller than the
        1/8 of the self.base-size.
        :param index: The index of the item the user want to delete.
        :return: None.
        :exception: The list should not be empty, or an AssertionError would be raised.
                    The given index must be within the range -len~len-1, or an IndexError would be raised.
        :pre-condition: An integer index must be given and the list must not be empty.
        :post-condition: The item at the given index would be deleted, and everything after the index would be move
                         forward.
        :Time-complexity: O(N) where N is the value of the given index.
        """
        assert not self.is_empty(), "The list is empty"
        if not ((index >= -len(self)) and (index < len(self))):
            raise IndexError("list index out of range")
        if index >= 0:
            start = index
        else:
            index = (-index) + (self.count - (-index)*2)
            start = index
        for i in range(start, self.count - 1):
            self[i] = self[i + 1]
        self.count -= 1
        self.shrink_dynamic()

    def sort(self, reverse):
        """
        This method sorts the ArrayBased list in ascending or descending order.
        :param reverse: An integer 1: if the sorting order is descedning, integer 0: if sorting order is ascending.
        :return: None.
        :exception: The reverse must be either 1 or 0, or an assertionError would be raised.
        :pre-condition: There must be aa reverse and it must be either 0 or 1.
        :post-condition: The list would be sorted in ascending order if reverse is 0, in descending order otherwise.
        "Time-complexity: The time-complexity of an insertion sort (can be found in file Task2_SortingSFunction).
        """
        assert reverse in [1, 0], "Invalid Parameter 'reverse'"
        if reverse == 0:
            insertion_sort_as(self)
        if reverse == 1:
            insertion_sort_de(self)

    def extend_dynamic(self):
        """
        This method double the size of the self.array.
        :param: None.
        :return: None.
        :exception: None.
        :pre-condition: The old array must be full to trigger this method.
        :post-condition: The size of the self.array would be doubled.
        :Time-complexity: O(N) where N is the size of the list.
        """
        if self.is_full() is True:
            tmp_list = []
            for i in range(len(self)):
                tmp_list.append(self[i])
            self.reset(self.base_size * 2)
            # got a extended list from here
            # put everything in the old list in
            for i in range(len(tmp_list)):
                self.append(tmp_list[i])

    def shrink_dynamic(self):
        """
        This method shrinks the size of self.array to half if the number of elements in array are fewer than 1/8 of the
        length. The size would never be smaller than 20.
        :param: None.
        :return: None.
        :exception: None.
        :pre-condition: The size must be bigger than 20 and the number of elements in array are fewer than 1/8 of the
                        length.
        :post-condition: The size would be shrinked to half.
        :Time-complexity: O(N) where N is the length of the self.array.
        """
        # the size can never smaller than 20
        if self.base_size > 20:
            if len(self) < len(self.array) / 8:
                tmp_list = []
                for i in range(len(self)):
                    tmp_list.append(self[i])
                self.reset(int(self.base_size / 2))
                for i in range(len(tmp_list)):
                    self.append(tmp_list[i])

    def __iter__(self):
        """
        This method iterate the object.
        :param: None.
        :return: An ArrayListIterator object.
        :exception: None.
        :pre-condition: None.
        :post-condition: An ArrayListIterator object would be returned.
        :Time-complexity: O(1)
        """
        return ArrayListIterator(self)


if __name__ == "__main__":
    test_obj = ArrayList()
    for j in range(5):
        test_obj.append(j)
    myIter = ArrayListIterator(test_obj)
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
    print(next(myIter))
