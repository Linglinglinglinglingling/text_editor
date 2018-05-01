

class LinkedIterator:

    def __init__(self, head):
        self.current = head

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            item = self.current.item
            self.current = self.current.next
            return item

    def __iter__(self):
        return self
