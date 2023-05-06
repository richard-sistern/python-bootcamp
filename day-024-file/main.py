file = open("./day-024-file/my_file.txt")
contents = file.read()
print(contents)

file.close() # Free resources

# Better way that automatically closes file resource
with open("./day-024-file/my_file.txt") as file2:
    contents = file2.read()
    print(contents)

# Append
with open("./day-024-file/my_file.txt", mode="a") as file3:
    file3.write("\npew pew pew")
