
import Task4


def test_array_file_reading():
    test_object = Task4.array_list_file_reading("try.txt")
    str(test_object)


def test_linked_file_reading():
    test_object = Task4.linked_list_file_reading("try1.txt")
    str(test_object)


if __name__ == "__main__":
    test_array_file_reading()
    test_linked_file_reading()