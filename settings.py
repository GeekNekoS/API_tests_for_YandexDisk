import os


with open(".env", "r") as file:
    lines = file.readlines()
    try:
        for line in lines:
            line = line.strip("\n")
            os.environ[line[:line.find("=")]] = line[line.find("=") + 1:]

    except ValueError:
        print("File '.env' is empty or doesn't exist!")
