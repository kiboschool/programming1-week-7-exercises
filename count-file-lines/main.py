import os

def show_line_counts():
    filename = input("Please enter a file name or path for line counting: ")
    lookup_value = input("Optional: Please enter a value for lookup - Press [Enter] for no value: ")

    if lookup_value:
        count = line_count(filename=filename, lookup_value=lookup_value)
        if count == -1:
            print("Error: Please enter a valid file name")
        else:
            print(f"Number of lines containing [{lookup_value}] is: {count}")
    else:
        count = line_count(filename=filename)
        if count == -1:
            print("Error: Please enter a valid file name")
        else:
            print(f"Number of lines in file: {count}")


def line_count(filename: str, lookup_value=None):
    """
    Counts the number of lines in file.
    If a lookup value is present, only counts lines that contain that value
    If the file does not exist, returns -1
    :param: filename: name of the file to count lines from
    :param: lookup_value: string value to lookup for within the file
    :return: int number of lines matching lookup value, or -1
    """
    count = 0
    if os.path.isfile(filename):
        with open(filename, 'r') as our_file:
            data = our_file.readlines()
        if lookup_value:
            for line in data:
                if lookup_value in line:
                    count += 1
            return count
        else:
            return len(data)
    else:
        return -1

if __name__ == "__main__":
    show_line_counts()
