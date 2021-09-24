fileFormat = ["JSON", "XML", "CSV"]


def convertFile(ext):
    newFileName = f"final_students.{ext}"
    with open("final_students.txt", "r") as f:
        with open(newFileName, "w") as n:
            n.write(f.read())
            print("File has been converted")


def serializeFile():
    selectedFormat = input(f"Please enter file type between {fileFormat}:")

    if selectedFormat == fileFormat[0]:
        convertFile(".json")

    elif selectedFormat == fileFormat[1]:
        convertFile(".xml")

    elif selectedFormat == fileFormat[2]:
        convertFile("_json.txt")

    else:
        print("Invalid file type")


serializeFile()
