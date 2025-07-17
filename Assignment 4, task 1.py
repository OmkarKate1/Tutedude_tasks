try:
    contents= open("sample.txt", "r")
    file_red= contents.read()
    print(file_red)
except FileNotFoundError:
    print("The file sample.txt was not found.")
