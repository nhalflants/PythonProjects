import glob

filepaths = glob.glob("files/*.txt")

for filepath in filepaths:
    with open(filepath, "r") as file:
        print(file.read())
