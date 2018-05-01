"""
@author: Lingling Yao
@since: 01/05/2018
@modified: 01/05/2018
@functionality: Task1: This file contains the iterator class for an ArrayBased List class.
"""


class ArrayListIterator:

    def __init__(self, current_list):
        self.current_list = current_list
        self.current_index = 0

    def __next__(self):
        if self.current_index == len(self.current_list):
            raise StopIteration
        else:
            item = self.current_list[self.current_index]
            self.current_index += 1
            return item

    def __iter__(self):
        return self
