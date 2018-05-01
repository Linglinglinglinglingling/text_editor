"""
@author: Lingling Yao
@since: 29/04/2018
@modified: 01/05/2018
@functionality: Task3: This file contains a LinkedList class.
"""


from Task3_NodeClass import Node
from Task3_iteratorClass import LinkedIterator
from Task3_SortingsFunction import insertion_sort_as
from Task3_SortingsFunction import insertion_sort_de


class LinkedList:

    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def reset(self):
        return self.__init__()

    def __len__(self):
        return self.count

    def __str__(self):
        string = ""
        current_node = self.head
        for _ in range(self.count):
            string += str(current_node.item) + "\n"
            current_node = current_node.next
        print(string)
        return string

    def __iter__(self):
        return LinkedIterator(self.head)

    def _get_node(self, index):
        if not (-len(self) <= index < len(self)):
            raise IndexError("Index out of range")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def insert(self, index, item):
        if not (-len(self) <= index < len(self)):
            raise IndexError("Index out of range")
        # insert to head
        if index == 0 or index == (-len(self)):
            self.head = Node(item, self.head)
            self.count += 1
        # insert to somewhere else
        else:
            if index > 0:
                index = index
            else:
                index = (-index) + (self.count - (-index) * 2)

            node = self._get_node(index - 1)
            node.next = Node(item, node.next)
            self.count += 1

    def append(self, item):
        if self.is_empty():
            self.head = Node(item, None)
            self.count += 1
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(item, None)
            self.count += 1

    def __getitem__(self, index):
        if not (-len(self) <= index < len(self)):
            raise IndexError("Index out of range")
        if index >= 0:
            index = index
        else:
            index = index = (-index) + (self.count - (-index) * 2)
        node = self._get_node(index)
        return node.item

    def __contains__(self, item):
        current_node = self.head
        while current_node is not None:
            if current_node.item == item:
                return True
            current_node = current_node.next
        return False

    def __setitem__(self, index, item):
        if not (-len(self) <= index < len(self)):
            raise IndexError("Index out of range")
        if index >= 0:
            index = index
        else:
            index = index = (-index) + (self.count - (-index) * 2)
        node = self._get_node(index)
        node.item = item

    def __eq__(self, other):
        if self.count == len(other):
            for i in range(self.count):
                if self[i] == other[i]:
                    continue
                else:
                    return False
            return True
        else:
            return False

    def remove(self, item):
        assert not self.is_empty(), "The list is empty"
        for i in range(self.count):
            if self[i] == item:
                self.delete(i)
                return
        raise ValueError("Item not found")

    def delete(self, index):
        if not (-len(self) <= index < len(self)):
            raise IndexError("Index out of range")
        assert not self.is_empty(), "The list is empty"
        if index == 0:
            self.head = self.head.next
        else:
            if index > 0:
                index = index
            if index < 0:
                index = index = (-index) + (self.count - (-index) * 2)
            node = self._get_node(index - 1)
            node.next = node.next.next
        self.count -= 1

    def sort(self, reverse):
        assert reverse in [1, 0], "Invalid Parameter 'reverse'"
        if reverse == 0:
            insertion_sort_as(self)
        if reverse == 1:
            insertion_sort_de(self)


if __name__ == "__main__":
    a_object = LinkedList()
    a_object.append(0)
    a_object.append(1)
    a_object.append(2)
    str(a_object)
    a_object.insert(0, 11)
    a_object.insert(2, 12)
    str(a_object)
    print(a_object[0])
    print(a_object[-1])
    print(11 in a_object)
    print(234 in a_object)
    a_object.delete(0)
    str(a_object)
    a_object.remove(12)
    str(a_object)