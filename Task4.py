
from Task2_ArrayListClass import ArrayList
from Task3_LinkedListClass import LinkedList


def array_list_file_reading(filename):
    archive_array = ArrayList()
    my_file = open(filename, "r")
    for line in my_file:
        line = line.strip("\n")
        archive_array.append(line)
    return archive_array

def linked_list_file_reading(filename):
    archive_linked = LinkedList()
    my_file = open(filename, "r")
    for line in my_file:
        line = line.strip("\n")
        archive_linked.append(line)
    return archive_linked


if __name__ == "__main__":
    array_list_file_reading("try.txt")
    linked_list_file_reading("try2.txt")
