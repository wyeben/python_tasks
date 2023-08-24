def get_file_extension(filename):
    parts = filename.split('.')
    if len(parts) > 1:
        return parts[-1]
    else:
        return "No file extension found"


filename = input("Enter a file name: ")
extension = get_file_extension(filename)
print("File extension:", extension)
