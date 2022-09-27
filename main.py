import os

# Size constants
KB = 1000
MB = KB * 1000
GB = MB * 1000

# initial bytes for filetypes
pdf = bytes.fromhex('25 50 44 46')
gif = bytes.fromhex('47 49 46')
png = bytes.fromhex('89 50 4E 47 0D 0A 1A 0A')
jpeg_start = bytes.fromhex('FF D8')
jpeg_end = bytes.fromhex('FF D9')
utf8_bom = bytes.fromhex('EF BB BF')

def file_info(filename):
    if not os.path.isfile(filename):
        return f"Error: File [{filename}] does not exist"
    else:
        result = ""
        result += f"File Statistics:\n"
        result += f"File Name: {filename}\n"
        result += f"File Size: {get_file_size(filename=filename)}\n"
        result += f"File Type: {get_file_type(filename=filename)}"
        return result

def get_file_size(filename: str) -> str:
    file_size = os.stat(filename).st_size

    if file_size < KB:
        return f"{file_size} bytes"
    elif file_size < MB:
        return f"{round(file_size / KB, 2)} KB"
    elif file_size < GB:
        return f"{round(file_size / MB, 2)} MB"
    else:
        return f"{round(file_size / GB, 2)} GB"


def get_file_type(filename: str) -> str:
    with open(filename, 'rb') as mystery_file:
        # read the first 10 bytes from the file
        starting_bytes = mystery_file.read(10)
        # read last 10 bytes
        mystery_file.seek(-10, os.SEEK_END)
        ending_bytes = mystery_file.read(10)

        if starting_bytes[:4] == pdf:
            return 'PDF'
        elif starting_bytes[:3] == gif:
            return 'GIF'
        elif starting_bytes[:8] == png:
            return 'PNG'
        elif starting_bytes[:3] == utf8_bom:
            return 'UTF-8 text with BOM'
        elif starting_bytes[:2] == jpeg_start and ending_bytes[-2:] == jpeg_end:
            return 'JPEG'
        else:
            return 'Unknown File Type'

# Run the fileinfo function on a provided filename
def main():
    filename = input("Enter a file name please: ")
    print(file_info(filename))

if __name__ == "__main__":
    main()
