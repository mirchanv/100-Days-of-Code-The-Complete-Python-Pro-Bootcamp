file = open("my_file.txt")

# read the file
file_contents = file.read()
print(file_contents)

# close file - to free up the resources
file.close()

# Another better way
def read_from_file():
    with open ("demo.txt", mode="r") as my_file:
        content = my_file.read()
        return content

# NOTE: when using the with keyword we do not manually have to close the file

# writing to file
def write_to_file():
    with open ("demo.txt", mode="a") as my_file:
        my_file.write("\nanother line written")
        print(f"Successfully written in {my_file.name}")

print(read_from_file())
write_to_file()


