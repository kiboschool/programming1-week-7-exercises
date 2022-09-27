# Binary File Info

In this exercise, you'll practice working with binary files, that aren't encoded text.

Write a program that accepts the name of a file from standard input, and prints out the following information about that file:

- name of the file (as it was entered to the program)
- how large is the file, in a nice format (specified below)
- detect if the file is of a certain type, by checking for common patterns in the bytes

## Nice filesize format

It's nice to use different units to convey the size, instead of having lots of digits.

For any filesize, choose from these units, so that the user sees the fewest number of digits in the output, keeping the numeric part of the output larger than 1.

B
KB = 1000B
MB = 1000MB
GB = 1000MB

So, if a file is 450,000,000 Bytes, your program should say that it is 450MB instead.

## Detecting the file type from a byte pattern

Different kinds of files often begin with a specific pattern of bytes.

Here are the ones that your program needs to be able to detect, and their byte patterns:

- PDF: first four bytes are 0x25 0x50 0x44 0x46
- GIF: first three bytes are 0x47 0x49 0x46
- JPEG image files begin with 0xFF 0xD8 and end with 0xFF 0xD9
- PNG image files begin with an 8-byte signature which identifies the file as a PNG file and allows detection of common file transfer problems: 0x89 0x50 0x4E 0x47 0x0D 0x0A 0x1A 0x0A
- UTF-8 encoded text files usually begin with the bytes 0xEF 0xBB 0xBF (called a Byte Order Mark, BOM)

Your program should print out the type of file it detects, or "Unknown file type" if none of these types match.

## Further Reading

See more filetype magic numbers at https://en.wikipedia.org/wiki/Magic_number_(programming)#In_files)

After you've finished the project, take a look at the library [filetype.py](https://github.com/h2non/filetype.py). It does the same kind of filetype checking that you implemented, but for a wide variety of types of files. Do you spot any similarities or differences between your code and the library code?
