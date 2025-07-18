import os

filename = "sample.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("Hello, file created!")
    print("File created.")
else:
    print("File already exists.")
