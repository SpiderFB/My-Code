# Reading user input file as in_file and  user output file as out_file

with open(input("Enter input file name: "), "rb") as in_file, open(input("Enter output file name: "), "wb") as out_file:
    # declaring an array to store file content for decoding
    new_arr = []
    for i in in_file.read():            # loop to catch each byte
        new_arr.append(i - 5)           # decoding each byte
    out_file.write(bytearray(new_arr))  # writing into file
