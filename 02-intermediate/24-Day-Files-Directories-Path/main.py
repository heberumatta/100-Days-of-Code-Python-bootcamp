# Files System
# Note: To use this path, in the terminal, you need to be in the same directory as this file.
f = open("./my_file.txt")
content = f.read()
print(content)

# If there is an "open" it need to be a "close".
f.close()

# There are a lot of ways to open a file, for example, you can use the "with" statement. This way, you don't need to close the file.
with open("./my_file.txt") as f:
    content = f.read()
    print(content)

# When you want to write to a file, you need to open it in write mode. If the file doesn't exist, it will be created.
with open("./my_file_created_with_write.txt", mode="w") as f:
    f.write("\nThis is a new line of text.\n")
    # content = f.read()   This will not work because the file is opened in write mode.

# Relative and Absolute Paths
# Relative paths are relative to the current working directory. Absolute paths are the full path from the root of the file system.

# Mail Merge Challenge
