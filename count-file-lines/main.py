import os

def show_line_counts():
    filename = input("Please enter a file name or path for line counting: ")

    lookup_value = input(
        "Optional: Please enter a value for lookup - Press [Enter] for no value: "
    )

    count = line_count(filename, lookup_value)

    if count == -1:
        print("Error: Please enter a valid file name")
    elif lookup_value == "":
        print(f"Number of lines in file: {count}")
    else:
        print(f"Number of lines containing [{lookup_value}] is: {count}")

def line_count(filename: str, lookup_value: str) -> int:
    """
    Counts the number of lines in file. 
    If a lookup value is present, only counts lines that contain that value
    If the file does not exist, returns -1 
    :param: filename: name of the file to count lines from
    :param: lookup_value: string value to lookup for within the file
    :return: int number of lines matching lookup value, or -1
    """
    if not os.path.exists(filename):
        return -1

    count = 0

    with open(filename, "r") as f:
        for line in f:

            # No lookup value → count everything
            if lookup_value == "":
                count += 1

            # Lookup value exists → only count matching lines
            elif lookup_value in line:
                count += 1
    return count

if __name__ == "__main__":
    show_line_counts()