import os

def list_files(directory):
    print("Files in directory:", directory)
    for file in os.listdir(directory):
        print(file)

if __name__ == "__main__":
    list_files(".")
