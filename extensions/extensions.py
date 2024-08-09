def main():
    file_name = input("File: ").strip()
    result = get_file_direction(file_name.lower())
    thisdict = { ".jpg": "image/jpeg",".jpeg": "image/jpeg", ".png": "image/png", ".pdf": "application/pdf",
                ".txt": "text/plain", ".zip": "application/zip", ".bin": "application/octet-stream",".gif": "image/gif"}
    print(thisdict.get(result, "application/octet-stream"))

def get_file_direction(file_name):
    file_extension = file_name.split(".")[-1]
    return "." + file_extension

main()
