"""
@author: Lingling Yao
@since: 26/04/2018
@modified: 01/05/2018
@functionality: Task1: This file contains a Array-based List class.
"""


from Task1_SortingsFunction import insertion_sort_as
from Task1_SortingsFunction import insertion_sort_de
from referential_array import build_array


class ArrayList:

    def __init__(self):
        """
            This is a constructor for class ArrayList.
            :param: None.
            :return: None.
            :exception: NONE.
            :pre-condition: A array, a counter.
            :post-condition: An array-based list object with a size 30 will be created.
            :complexity: O(1)
            """
        self.array = build_array(50)
        self.count = 0

    def __str__(self):
        """
            This method convert every element in list into string and display it line by line.
            :param: None.
            :return: Boolean: If the printing finishes.
            :exception: NONE.
            :pre-condition: None.
            :post-condition: Every element in list would be printed line by line and boolean True would be returned
                             after printing.
            :complexity: TBC
            """
        for index in range(len(self)):
            string = str(self.array[index])
            print(string)
        return True

    def __len__(self):
        """
            This method return the length of the list.
            :param: None.
            :return: self.count: The number of the elements in the list.
            :exception: NONE.
            :pre-condition: None.
            :post-condition: The self.count would be returned.
            :complexity: TBC
            """
        return self.count

    def __contains__(self, item):
        """
            This method checks if a given element is in the list.
            :param: item: The given item to be checked.
            :return: Boolean: True if the element is found in list, False otherwise.
            :exception: An exception would be rised if the list is empty.
            :pre-condition: An item has to be given by user and the list should not be empty.
            :post-condition: True would be returned if the element is in the list, otherwise False would be returned.
            :complexity: TBC
            """
        assert not self.count == 0, "The list is empty"
        for index in range(len(self)):
            if self.array[index] == item:
                return True
        return False

    def __getitem__(self, index):
        """
            This method get the item at a given index.
            :param: index: The given index to interact with.
            :return: item: the item at the given index.
            :exception: An exception would be raised if the index is out of range.
            :pre-condition: An valid index has to be given by user.
            :post-condition: The item at the given index would be returned.
            :complexity: TBC
            """
        if not ((index >= -len(self)) or (index < len(self))):
            raise IndexError("list index out of range")
        # positive index
        if index >= 0:
            return self.array[index]
        # negative index
        else:
            index = (-index) + (self.count - (-index)*2)
            return self.array[index]

    def append(self, item):
        """
            This method add a given item to the end of the list
            :param: item: An item given be the user.
            :return: Boolean: If the item is added successfully.
            :exception: An exception would be raised if the list is full(in this case: already have 50 elements).
            :pre-condition: A item given and a ArrayList object which has less than 50 elements.
            :post-condition: The given item would be added to the end of the list.
                             An expection would be raise if there are already 50 elements in the list.
            :complexity: TBC
            """
        assert self.count < 50, "The list is full"
        self.array[self.count] = item
        self.count += 1
        return True

    def __setitem__(self, index, item):
        if not ((index >= -len(self)) or (index < len(self))):
            raise IndexError("list index out of range")
        if index >= 0:
            self.array[index] = item
        else:
            index = (-index) + (self.count - (-index)*2)
            self.array[index] = item
        return True

    def __eq__(self, other):
        if len(self) == len(other):
            flag = 0
            for index in range(len(self)):
                    if self[index] == other[index]:
                        flag += 1
            if flag == len(self):
                return True
            else:
                return False
        else:
            return False

    def insert(self, index, item):
        assert self.count < 50, "The list is full"
        if not ((index >= -len(self)) and (index < len(self))):
            raise IndexError("list index out of range")
        # positive index
        if index >= 0:
            start = index
        # otherwise
        else:
            index = (-index) + (self.count - (-index)*2)
            start = index
        self.count += 1
        for i in range(self.count - 1, start - 1, -1):
            self[i + 1] = self[i]
        self[index] = item
        return True

    def remove(self, item):
        for i in range(len(self)):
            if self[i] == item:
                start = i
                for j in range(start, self.count):
                    self[j] = self[j + 1]
                self.count -= 1
                return True
        raise ValueError("item not found")

    def delete(self, index):
        if not ((index >= -len(self)) or (index < len(self))):
            raise IndexError("list index out of range")
        if index >= 0:
            start = index
        else:
            index = (-index) + (self.count - (-index)*2)
            start = index
        for i in range(start, len(self)):
            self[i] = self[i + 1]
        self.count -= 1
        return True

    def sort(self, reserve):
        if reserve == 0:
            insertion_sort_as(self)
        else:
            insertion_sort_de(self)
        return True
